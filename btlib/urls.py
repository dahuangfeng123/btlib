from django.conf.urls import patterns, include, url
from btlib.feeds import Feed

urlpatterns = patterns('django.contrib.flatpages.views',
                       url(r'^$', 'flatpage', {'url': '/'}, name='btlib_index'),
                       url(r'^about/$', 'flatpage', {'url': '/about/'}, name='btlib_about'),
                       url(r'^disclaimer/$', 'flatpage', {'url': '/disclaimer/'}, name='btlib_disclaimer'),
)

urlpatterns += patterns('btlib.views',
                        url(r'^form/get/(?P<frm>\w+)(?:/(?P<obj>\d+))?/$', 'form_get', name='btlib_form_get'),
                        url(r'^form/set/(?P<frm>\w+)(?:/(?P<obj>\d+))?/$', 'form_set', name='btlib_form_set'),
                        url(r'^catalogue/$', 'catalogue', name='btlib_catalogue'),
                        url(r'^catalogue/novel/(?P<nid>\d+)/$', 'catalogue_novel', name='btlib_catalogue_novel'),
                        url(r'^catalogue/volume/(?P<vid>\d+)/$', 'catalogue_volume', name='btlib_catalogue_volume'),
)

urlpatterns += patterns("",
                        url(r'^feed/$', Feed(), name='btlib_feed'),
)