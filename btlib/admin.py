from django.contrib import admin
from btlib.models import *


class ProjectStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','iso')
    search_fields = ['name','iso']

class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class NameLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ['name']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso')
    search_fields = ['name']

"""
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'volume', 'cover', 'created')
    search_fields = ['__unicode__', 'volume__name', 'info']
    list_filter = ('cover', 'modified')
"""

admin.site.register(Author)
admin.site.register(Illustrator)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(ProjectStatus)
admin.site.register(ProjectType)
admin.site.register(Language)
admin.site.register(Novel)
admin.site.register(Volume)
admin.site.register(Chapter)
admin.site.register(Project)
admin.site.register(ProjectTranslation)
admin.site.register(NovelTranslation)
admin.site.register(VolumeTranslation)
admin.site.register(ChapterTranslation)
admin.site.register(Revision)
admin.site.register(Note)
admin.site.register(Image)
