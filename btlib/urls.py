from django.conf.urls import patterns, include, url

urlpatterns = patterns('btlib.views',
    url(r'^$', 'index', name='btlib_index'),
    url(r'^form/get/(?P<frm>\w+)(?:/(?P<obj>\d+))?/$', 'form_get', name='btlib_form_get'),
    url(r'^form/set/(?P<frm>\w+)(?:/(?P<obj>\d+))?/$', 'form_set', name='btlib_form_set'),
    url(r'^catalogue/$', 'catalogue', name='btlib_catalogue'),
    url(r'^catalogue/novel/(?P<nid>\d+)/$', 'catalogue_novel', name='btlib_catalogue_novel'),
    url(r'^catalogue/volume/(?P<vid>\d+)/$', 'catalogue_volume', name='btlib_catalogue_volume'),
)