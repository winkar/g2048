from django.conf.urls import patterns, include, url
from view import *
from settings import STATIC_PATH

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'g2048.views.home', name='home'),
    # url(r'^g2048/', include('g2048.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
    url(r'^start/$',start),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':STATIC_PATH}),
    url(r'^gaming/(.*)/$',gaming),
)
