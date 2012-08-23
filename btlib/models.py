from django.db import models

# Create your models here.

class Series(models.Model):
      name = models.CharField(max_length = 255)
      author = models.CharField(max_length = 200)
      def __unicode__(self):
        return self.name

class Volume(models.Model):
      series = models.ForeignKey('Series')
      number = models.PositiveIntegerField()
      def __unicode__(self):
        return self.series.name +':'+ str(self.number)

class Chapter(models.Model):
      volume = models.ForeignKey('Volume')
      number = models.PositiveIntegerField()
      def __unicode__(self):
        return self.volume.series.name +":" + str(self.volume.number) + '-' + str(self.number)

class Language(models.Model):
      name = models.CharField(max_length = 255)
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
        chap_list = Translation.objects.filter( chapter__volume = self.volume ).filter( language = self.language )
        chap_list = sorted(chap_list, key=lambda chap: chap.chapter.number)
        return chap_list
      def __unicode__(self):
        return self.name

class Translation(models.Model):
      name = models.CharField(max_length = 255)
      language = models.ForeignKey('Language')
      chapter = models.ForeignKey('Chapter')
      text = models.TextField()
      @models.permalink
      def get_absolute_url(self):
        return ('btlib.views.chapter',(),{'chap':self.pk})
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
          series = SeriesTrans.objects.filter( series = self.chapter.volume.series ).filter(language = self.language)
          if series:
             return series[0]
          else: # If this happens, someone forgot to define the series translation before adding the translated chapters...
             return None
      def __unicode__(self):
        return self.name

class SeriesTrans(models.Model):
      name = models.CharField(max_length = 255)
      language = models.ForeignKey('Language')
      series = models.ForeignKey('Series')
      synopsis = models.TextField()
      @models.permalink
      def get_absolute_url(self):
        return ('btlib.views.series',(),{'ln':self.pk})
      def get_volumes(self):
        vol_list = VolTrans.objects.filter( volume__series = self.series ).filter( language = self.language )
        vol_list = sorted(vol_list, key=lambda vol: vol.volume.number)
        return vol_list
      def __unicode__(self):
        return self.name

class Image(models.Model):
      volume = models.ForeignKey('Volume')
      image = models.ImageField(upload_to = 'images')
      subtext = models.TextField()
      def __unicode__(self):
        return self.image.name
      def get_absolute_url(self):
        return self.image.get_absolute_url()
