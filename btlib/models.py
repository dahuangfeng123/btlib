from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from diff_match_patch import diff_match_patch
from btlib.functions import btParse
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 256)
    def __unicode__(self):	  	
        return self.name

class Illustrator(models.Model):
    name = models.CharField(max_length = 256)
    def __unicode__(self):	  	
        return self.name

class Novel(models.Model):
    name = models.CharField(max_length = 255)
    author = models.ForeignKey(Author)
    author = models.ForeignKey(Illustrator)
    def __unicode__(self):
        return self.name

class Volume(models.Model):
    novel = models.ForeignKey(Novel)
    number = models.PositiveIntegerField()
    isbn = models.CharField(max_length=17, blank=True)
    year = models.PositiveSmallIntegerField(max_length=4)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def uuid_gen():
        return uuid4() # need to change this, I think...
<<<<<<< HEAD
    uuid = models.SlugField(max_length=36, unique=True, default=uuid4())
=======
    uuid = models.SlugField(max_length=36, unique=True, default=uuid_gen())
>>>>>>> 3916c64e8bb0a5a1c856376d7c23eeb97a77a26c
    def __unicode__(self):
        return self.novel.name +':'+ str(self.number)

class Chapter(models.Model):
    volume = models.ForeignKey('Volume')
    number = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.volume.novel.name +":" + str(self.volume.number) + '-' + str(self.number)

class Language(models.Model):
    name = models.CharField(max_length = 255)
    iso = models.SlugField(max_length=2, unique=True)
    @models.permalink
    def get_absolute_url(self):
        return ('btlib.views.language',(),{'lang':self.pk})
    def __unicode__(self):
        return self.name

class VolTrans(models.Model):
    name = models.CharField(max_length = 255)
    volume = models.ForeignKey('Volume')
    language = models.ForeignKey('Language')
    def get_chapters(self):
        chap_list = Translation.objects.filter( chapter__volume = self.volume ).filter( language = self.language ) # this could probably be turned into one filter with a comma...
        chap_list = sorted(chap_list, key=lambda chap: chap.chapter.number)
        return chap_list
    def __unicode__(self):
        return self.name

class Translation(models.Model):
    name = models.CharField(max_length = 255)
    language = models.ForeignKey(Language)
    chapter = models.ForeignKey(Chapter)
    translator = models.ForeignKey(User)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    shown = models.ForeignKey('Revision', on_delete = models.Protect, null=True, blank=True)
=======
>>>>>>> 3916c64e8bb0a5a1c856376d7c23eeb97a77a26c
    @models.permalink
    def get_absolute_url(self):
        return ('btlib.views.chapter',(),{'chap':self.pk})
    def save(self, *args, **kwargs):
        patcher = diff_match_patch()
        plist = [self.shown.diff,]
        parent = self.shown.based_off
        while parent:
            plist += parent.diff
            parent = parent.based_off
        text = patcher.patch_apply(reversed(plist),’’)
        self.shown_text = btParse(text)
        super(Translation, self).save(*args, **kwargs)
    def get_next(self):
        next = Translation.objects.filter( chapter__volume = self.chapter.volume ).filter( chapter__number = self.chapter.number + 1).filter( language = self.language)
        if next:
           return next[0]
        else:
           return None
    def get_prev(self):
        next = Translation.objects.filter( chapter__volume = self.chapter.volume ).filter( chapter__number = self.chapter.number - 1).filter( language = self.language)
        if next:
           return next[0]
        else:
           return None
    def get_series(self):
          series = Project.objects.filter( novel = self.chapter.volume.novel ).filter(language = self.language)
          if series:
             return series[0]
          else: # If this happens, someone forgot to define the series translation before adding the translated chapters...
             return None
    def __unicode__(self):
        return self.name

class Revision(models.Model):
    translation = models.ForeignKey(Translation)
    submitter = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    diff = models.TextField()
    based_off = models.ForeignKey('self', blank=True, null=True)

class Note(models.Model):
    rev = models.ForeignKey(Revision)
    text = models.TextField()
    

class Project_Type(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):	  	
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 256)
    language = models.ForeignKey(Language)
    novel = models.ForeignKey(Novel)
    project_type = models.ForeignKey(Project_Type)
    supervisor = models.ForeignKey(User)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    @models.permalink
    def get_absolute_url(self):
      return ('btlib.views.novel',(),{'ln':self.pk})
    def get_volumes(self):
        vol_list = VolTrans.objects.filter( volume__novel = self.novel ).filter( language = self.language )
        vol_list = sorted(vol_list, key=lambda vol: vol.volume.number)
        return vol_list
    def __unicode__(self):
        return self.name

class Image(models.Model):
    volume = models.ForeignKey('Volume', blank=True)
    image = models.ImageField(upload_to = 'images')
    subtext = models.TextField()
    def __unicode__(self):
        return self.image.name
    def get_absolute_url(self):
        return self.image.get_absolute_url()
