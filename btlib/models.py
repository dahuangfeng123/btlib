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
