from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from uuid import uuid4
from diff_match_patch import diff_match_patch
from btlib.functions import btParse

"""
Make out of Chapter Type a Model that will be used in chapter and create a script that will automatically import the entries on first run.
Further de/activate field should be added.

Rethink the idea about adding parts to chapters.


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

"""
Active, Inactive, Frozen, Deleted, Licensed
"""


class ProjectStatus(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name


"""
Language Model

Language model should follow the ISO 639-1 standard and probably integrate these on the first run.

Returns Name field.
"""


class Language(models.Model):
    name = models.CharField(max_length=255)
    iso = models.SlugField(max_length=2, unique=True)

    def __unicode__(self):
        return self.name


"""
#################
#CATALOGUE START#
#################
"""

"""
Author Model

Contains the Name of the potential Author, the URI to his/her Blog and his Bio.

Name field is obligatory.
Bio and URL are optional.

Returns Name field.
"""


class Author(models.Model):
    name = models.CharField(max_length=256, unique=True)
    bio = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name


"""
Illustrator Model

Contains the Name of the potential Illustrator, the URI to his/her Blog and his Bio.

Name field is obligatory.
Bio and URL are optional.

Returns Name field.
"""


class Illustrator(models.Model):
    name = models.CharField(max_length=256, unique=True)
    bio = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name


"""
Genre Model

Contains the Name of the possible Genre

Name field is obligatory.
Max length is 256 characters.

Returns Name field.
"""


class Genre(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name


"""
Publisher Model

Contains the Name of the Novel's publisher

Name field is obligatory.
Max length is 256 characters.

Returns Name field.
"""


class Publisher(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(max_length=500, blank=True)

    def __unicode__(self):
        return self.name


"""
Novel Model

Under Novel is to understand a publication of multiple Volumes that run under one Name.

Name field should be, if possible, the original Title. In it's original language.
Romajin field is for the romanification of the field Name

Fields illustrator, author, genre and publisher are liked to their own models.

Returns Name field.
"""


class Novel(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    romajin = models.CharField(max_length=255)
    illustrator = models.ForeignKey(Illustrator, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


"""
Volume Model

Volume model depends on Novel model.

Name field should be, if possible, the original Title. In it's original language.
Romajin field is for the romanification of the field Name

Number is to be used if the volume has a numerical counting. If not, use the order field, to order the novels.

Order field is to be used to order the volumes in a specific order. Accepts float numbers(some people like this...).

ISBN field accepts max. 17 characters.(for now)

Year field it to be used to derterminate the date of publication of the volume.

Returns (to be changed)
"""


class Volume(models.Model):
    name = models.CharField(max_length=255)
    romajin = models.CharField(max_length=255)
    novel = models.ForeignKey(Novel)
    number = models.FloatField(blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True)
    year = models.PositiveSmallIntegerField(max_length=4)# make out of it month and year
    order = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.SlugField(max_length=36, unique=True, default=uuid4())

    def save(self, *args, **kwargs):
        self.uuid = uuid4()
        super(Volume, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.novel.name + ':' + str(self.number)


"""
Chapter Model

Chapter model is depends on Volume model.

Name field should be, if possible, the original Title. In it's original language.
Romajin field is for the romanification of the field Name

Number is to be used if the volume has a numerical counting. If not, use the order field, to order the novels.

Order field is to be used to order the volumes in a specific order. Accepts float numbers.

Returns (to be changed)
"""


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    romajin = models.CharField(max_length=255)
    volume = models.ForeignKey(Volume)
    number = models.FloatField(blank=True, null=True)
    order = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.volume.novel.name + ":" + str(self.volume.number) + '-' + str(self.name)


"""
Project Model

Used to bundle multiple novels in case if they are cannonical.

"""


class Project(models.Model):
    name = models.CharField(max_length=255)
    novel = models.ManyToManyField(Novel)
    admin = models.ForeignKey(User)
    status = models.ForeignKey(ProjectStatus)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


"""
#################
# CATALOGUE END #
#################
"""

"""
#########################
#TRANSLATION LAYER START#
#########################
"""


class ProjectTranslation(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project)
    language = models.ForeignKey(Language)
    discription = models.TextField()
    type = models.ForeignKey(ProjectType)
    supervisor = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class NovelTranslation(models.Model):
    name = models.CharField(max_length=255)
    projecttranslation = models.ForeignKey(ProjectTranslation)
    novel = models.ForeignKey(Novel)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class VolumeTranslation(models.Model):
    name = models.CharField(max_length=255)
    noveltranslation = models.ForeignKey(NovelTranslation)
    volume = models.ForeignKey(Volume)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class ChapterTranslation(models.Model):
    name = models.CharField(max_length=255)
    noveltranslation = models.ForeignKey(VolumeTranslation)
    chapter = models.ForeignKey(Chapter)
    text = models.TextField()
    translator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    shown = models.ForeignKey('Revision', on_delete=models.PROTECT, null=True, blank=True,
                              related_name="shown+")

    def save(self, *args, **kwargs):
        patcher = diff_match_patch()
        plist = [self.shown.diff, ]
        parent = self.shown.based_off
        while parent:
            plist += parent.diff
            parent = parent.based_off
        text = patcher.patch_apply(reversed(plist), '')
        self.text = btParse(text)
        super(ChapterTranslation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Revision(models.Model):
    chaptertranslation = models.ForeignKey(ChapterTranslation)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    diff = models.TextField()
    based_off = models.ForeignKey('self', blank=True, null=True, related_name="revision_set")


class Note(models.Model):
    rev = models.ForeignKey(Revision)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


"""
#########################
# TRANSLATION LAYER END #
#########################
"""


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    subtext = models.TextField()
    user = models.ForeignKey(User)
    novel = models.ForeignKey(Novel, null=True, blank=True)
    volume = models.ForeignKey(Volume, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image.name
