from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'btlib.views.index'),
    url(r'^series/(?P<ln>\d+)', 'btlib.views.series'),
    url(r'^lang/(?P<lang>\d+)', 'btlib.views.language'),
    url(r'^read/(?P<chap>\d+)', 'btlib.views.chapter'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
