from django.shortcuts import render_to_response, get_object_or_404
from btlib.models import *
from django.conf import settings
# Create your views here.

def index(request): #return a list of volumes in default language (english), and alternate languages
    ln_list = Project.objects.filter(language__pk=settings.MAIN_LN_LANG)
    lang_list = Language.objects.exclude(pk=settings.MAIN_LN_LANG)
    return render_to_response('btlib/index.html', {'ln_list': ln_list, 'lang_list': lang_list})


def novel(request, ln):
    ln = get_object_or_404(Project, pk=ln)
    lang = SeriesTrans.objects.filter(series=ln.series).exclude(language=ln.language)
    return render_to_response('btlib/series.html', {'ln': ln, 'langs': lang})


def language(request, lang): #return a list of volumes in given language, and alternate languages
    ln_list = Project.objects.filter(language__pk=lang)
    lang_list = Language.objects.exclude(pk=lang)
    return render_to_response('btlib/lang.html', {'ln_list': ln_list, 'lang_list': lang_list})


def chapter(request, chap):
    ch = get_object_or_404(Translation, pk=chap)
    next = Translation.objects.filter(chapter__volume=ch.chapter.volume).filter(
        chapter__number=ch.chapter.number + 1).filter(language=ch.language)
    next = ch.get_next()
    prev = ch.get_prev()
    return render_to_response('btlib/chapter.html', {'chap': ch, 'next': next, 'prev': prev})


def api_base(request):
    pass
