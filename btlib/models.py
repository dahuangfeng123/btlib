from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from uuid import uuid4
from diff_match_patch import diff_match_patch
from btlib.functions import btParse

"""
Make out of Chapter Type a Model that will be used in chapter and create a script that will automatically import the entries on first run.
Further de/activate field should be added.

Rethink the idea about adding parts to chapters.3


"""
CHAPTER_TYPE = (
    ('CH', 'Chapter'),
    ('PL', 'Prologue'),
    ('EL', 'Epilogue'),
    ('FW', 'Foreword'),
    ('PF', 'Preface'),
    ('ID', 'Introduction'),
    ('AW', 'Afterword'),
    ('PS', 'Postscript'),
    ('FN', 'Footnotes'),
    ('EN', 'End Notes'),
)


class Author(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    url = models.URLField(max_length = 500, blank = True)

    def __unicode__(self):
        return self.name


class Illustrator(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    url = models.URLField(max_length = 500, blank = True)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    url = models.URLField(max_length = 500, blank = True)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    url = models.URLField(max_length = 500, blank = True)

    def __unicode__(self):
        return self.name


"""
Active, Inactive, Frozen, Deleted, Licensed
"""
class ProjectStatus(models.Model):
    name = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name


"""
Language model should follow the ISO 639-1 standard and probably integrate these on the first run
"""
class Language(models.Model):
    name = models.CharField(max_length = 255)
    iso = models.SlugField(max_length = 2, unique = True)

    def __unicode__(self):
        return self.name


class Novel(models.Model):
    name = models.CharField(max_length = 255)
    author = models.ForeignKey(Author)
    romajin = models.CharField(max_length = 255)
    illustrator = models.ForeignKey(Illustrator, blank = True, null = True)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(max_length = 255)
    romajin = models.CharField(max_length = 255)
    novel = models.ForeignKey(Novel)
    number = models.FloatField(blank = True, null = True)
    isbn = models.CharField(max_length = 17, blank = True)
    year = models.PositiveSmallIntegerField(max_length = 4)# make out of it month and year
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    uuid = models.SlugField(max_length = 36, unique = True, default = uuid4())

    def save(self, *args, **kwargs):
        self.uuid = uuid4()
        super(Volume, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.novel.name + ':' + str(self.number)


class Chapter(models.Model):
    name = models.CharField(max_length = 255)
    romajin = models.CharField(max_length = 255)
    volume = models.ForeignKey(Volume)
    number = models.FloatField(blank = True, null = True)
    order = models.FloatField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.volume.novel.name + ":" + str(self.volume.number) + '-' + str(self.number)


class Project(models.Model):
    name = models.CharField(max_length = 255)
    novel = models.ManyToManyField(Novel)
    admin = models.ForeignKey(User)
    status = models.ForeignKey(ProjectStatus)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


class ProjectTrans(models.Model):
    name = models.CharField(max_length = 255)
    project = models.ForeignKey(Project)
    language = models.ForeignKey(Language)
    discription = models.TextField()
    type = models.ForeignKey(ProjectType)
    supervisor = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


class NovelTrans(models.Model):
    name = models.CharField(max_length = 255)
    projecttrans = models.ForeignKey(ProjectTrans)
    novel = models.ForeignKey(Novel)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


class VolumeTrans(models.Model):
    name = models.CharField(max_length = 255)
    noveltrans = models.ForeignKey(NovelTrans)
    volume = models.ForeignKey(Volume)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


class ChapterTrans(models.Model):
    name = models.CharField(max_length = 255)
    noveltrans = models.ForeignKey(VolumeTrans)
    chapter = models.ForeignKey(Chapter)
    text = models.TextField()
    translator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    shown = models.ForeignKey('Revision', on_delete = models.PROTECT, null = True, blank = True,
                              related_name = "shown+")

    def save(self, *args, **kwargs):
        patcher = diff_match_patch()
        plist = [self.shown.diff, ]
        parent = self.shown.based_off
        while parent:
            plist += parent.diff
            parent = parent.based_off
        text = patcher.patch_apply(reversed(plist), '')
        self.text = btParse(text)
        super(ChapterTrans, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Revision(models.Model):
    chaptertrans = models.ForeignKey(ChapterTrans)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User)
    diff = models.TextField()
    based_off = models.ForeignKey('self', blank = True, null = True, related_name = "revision_set")


class Note(models.Model):
    rev = models.ForeignKey(Revision)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)


class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    subtext = models.TextField()
    user = models.ForeignKey(User)
    novel = models.ForeignKey(Novel, null=True, blank=True)
    volume = models.ForeignKey(Volume, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.image.name
