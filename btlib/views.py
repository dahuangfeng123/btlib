from django.shortcuts import render_to_response, get_object_or_404, redirect
from btlib.models import *
from btlib.forms import *
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return None


def catalogue(request):
    novels = Novel.objects.all().select_related('author', 'illustrator', 'publisher').prefetch_related(
        'genre').order_by('romajin', 'name')
    return render_to_response('btlib/catalogue.html', {'novels':novels}, context_instance = RequestContext(request))


def catalogue_novel(request, nid):
    novel = get_object_or_404(Novel, id = nid)
    return render_to_response('btlib/catalogue.html', {'novel':novel}, context_instance = RequestContext(request))


def catalogue_volume(request, vid):
    return None


#@login_required(login_url = '/accounts/login/')
def form_set(request, frm, obj=None):
    if 'Author' in frm:
        if obj is not None:
            change = get_object_or_404(Author, id = obj)
            form = FormAuthor(request.POST or None, instance = change)
        else:
            form = FormAuthor(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Illustrator' in frm:
        if obj is not None:
            change = get_object_or_404(Illustrator, id = obj)
            form = FormIllustrator(request.POST or None, instance = change)
        else:
            form = FormIllustrator(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Genre' in frm:
        if obj is not None:
            change = get_object_or_404(Genre, id = obj)
            form = FormGenre(request.POST or None, instance = change)
        else:
            form = FormGenre(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Publisher' in frm:
        if obj is not None:
            change = get_object_or_404(Publisher, id = obj)
            form = FormPublisher(request.POST or None, instance = change)
        else:
            form = FormPublisher(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'ProjectStatus' in frm:
        if obj is not None:
            change = get_object_or_404(ProjectStatus, id = obj)
            form = FormProjectStatus(request.POST or None, instance = change)
        else:
            form = FormProjectStatus(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'ProjectType' in frm:
        if obj is not None:
            change = get_object_or_404(ProjectType, id = obj)
            form = FormProjectType(request.POST or None, instance = change)
        else:
            form = FormProjectType(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Language' in frm:
        if obj is not None:
            change = get_object_or_404(Language, id = obj)
            form = FormLanguage(request.POST or None, instance = change)
        else:
            form = FormLanguage(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Novel' in frm:
        if obj is not None:
            change = get_object_or_404(Novel, id = obj)
            form = FormNovel(request.POST or None, instance = change)
        else:
            form = FormNovel(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Volume' in frm:
        if obj is not None:
            change = get_object_or_404(Volume, id = obj)
            form = FormVolume(request.POST or None, instance = change)
        else:
            form = FormVolume(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Chapter' in frm:
        if obj is not None:
            change = get_object_or_404(Chapter, id = obj)
            form = FormChapter(request.POST or None, instance = change)
        else:
            form = FormChapter(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Project' in frm:
        if obj is not None:
            change = get_object_or_404(Project, id = obj)
            form = FormProject(request.POST or None, instance = change)
        else:
            form = FormProject(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'ProjectTrans' in frm:
        if obj is not None:
            change = get_object_or_404(ProjectTrans, id = obj)
            form = FormProjectTrans(request.POST or None, instance = change)
        else:
            form = FormProjectTrans(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'NovelTrans' in frm:
        if obj is not None:
            change = get_object_or_404(NovelTrans, id = obj)
            form = FormNovelTrans(request.POST or None, instance = change)
        else:
            form = FormNovelTrans(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'VolumeTrans' in frm:
        if obj is not None:
            change = get_object_or_404(VolumeTrans, id = obj)
            form = FormVolumeTrans(request.POST or None, instance = change)
        else:
            form = FormVolumeTrans(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'ChapterTrans' in frm:
        if obj is not None:
            change = get_object_or_404(ChapterTrans, id = obj)
            form = FormChapterTrans(request.POST or None, instance = change)
        else:
            form = FormChapterTrans(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Revision' in frm:
        if obj is not None:
            change = get_object_or_404(Revision, id = obj)
            form = FormRevision(request.POST or None, instance = change)
        else:
            form = FormRevision(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Note' in frm:
        if obj is not None:
            change = get_object_or_404(Note, id = obj)
            form = FormNote(request.POST or None, instance = change)
        else:
            form = FormNote(request.POST or None)
        if form.is_valid():
            form.save()

    elif 'Image' in frm:
        if obj is not None:
            change = get_object_or_404(Image, id = obj)
            form = FormImage(request.POST or None, instance = change)
        else:
            form = FormImage(request.POST or None)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


#@login_required(login_url = '/accounts/login/')
def form_get(request, frm, obj = None):
    if 'Author' == frm:
        if obj is not None:
            entry = get_object_or_404(Author, id = obj)
            form = FormAuthor(instance = entry)
        else:
            form = FormAuthor()
    elif 'Illustrator' == frm:
        if obj is not None:
            entry = get_object_or_404(Illustrator, id = obj)
            form = FormIllustrator(instance = entry)
        else:
            form = FormIllustrator()
    elif 'Genre' == frm:
        if obj is not None:
            entry = get_object_or_404(Genre, id = obj)
            form = FormGenre(instance = entry)
        else:
            form = FormGenre()
    elif 'Publisher' == frm:
        if obj is not None:
            entry = get_object_or_404(Publisher, id = obj)
            form = FormPublisher(instance = entry)
        else:
            form = FormPublisher()
    elif 'ProjectStatus' == frm:
        if obj is not None:
            entry = get_object_or_404(ProjectStatus, id = obj)
            form = FormProjectStatus(instance = entry)
        else:
            form = FormProjectStatus()
    elif 'ProjectType' == frm:
        if obj is not None:
            entry = get_object_or_404(ProjectType, id = obj)
            form = FormProjectType(instance = entry)
        else:
            form = FormProjectType()
    elif 'Language' == frm:
        if obj is not None:
            entry = get_object_or_404(Language, id = obj)
            form = FormLanguage(instance = entry)
        else:
            form = FormLanguage()
    elif 'Novel' == frm:
        if obj is not None:
            entry = get_object_or_404(Novel, id = obj)
            form = FormNovel(instance = entry)
        else:
            form = FormNovel()
    elif 'Volume' == frm:
        if obj is not None:
            entry = get_object_or_404(Volume, id = obj)
            form = FormVolume(instance = entry)
        else:
            form = FormVolume()
    elif 'Chapter' == frm:
        if obj is not None:
            entry = get_object_or_404(Chapter, id = obj)
            form = FormChapter(instance = entry)
        else:
            form = FormChapter()
    elif 'Project' == frm:
        if obj is not None:
            entry = get_object_or_404(Project, id = obj)
            form = FormProject(instance = entry)
        else:
            form = FormProject()
    elif 'ProjectTrans' == frm:
        if obj is not None:
            entry = get_object_or_404(ProjectTrans, id = obj)
            form = FormProjectTrans(instance = entry)
        else:
            form = FormProjectTrans()
    elif 'NovelTrans' == frm:
        if obj is not None:
            entry = get_object_or_404(NovelTrans, id = obj)
            form = FormNovelTrans(instance = entry)
        else:
            form = FormNovelTrans()
    elif 'VolumeTrans' == frm:
        if obj is not None:
            entry = get_object_or_404(VolumeTrans, id = obj)
            form = FormVolumeTrans(instance = entry)
        else:
            form = FormVolumeTrans()
    elif 'ChapterTrans' == frm:
        if obj is not None:
            entry = get_object_or_404(ChapterTrans, id = obj)
            form = FormChapterTrans(instance = entry)
        else:
            form = FormChapterTrans()
    elif 'Revision' == frm:
        if obj is not None:
            entry = get_object_or_404(Revision, id = obj)
            form = FormRevision(instance = entry)
        else:
            form = FormRevision()
    elif 'Note' == frm:
        if obj is not None:
            entry = get_object_or_404(Note, id = obj)
            form = FormNote(instance = entry)
        else:
            form = FormNote()
    elif 'Image' == frm:
        if obj is not None:
            entry = get_object_or_404(Image, id = obj)
            form = FormImage(instance = entry)
        else:
            form = FormImage()
    if form:
        return render_to_response('btlib/form.html', {'form': form, 'key': form},
                                  ontext_instance = RequestContext(request))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
