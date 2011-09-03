# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^short_url/(?P<secret>\S+)/$', 'urlshortener.views.create_shorturl'),
    url(r'^(?P<shortid>\S+)\+/$', 'urlshortener.views.get_actualurl'),
    url(r'^(?P<shortid>\S+)/$', 'urlshortener.views.open_shorturl'),
)
