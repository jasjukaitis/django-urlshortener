# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('shortid', 'url', 'views')
    list_display_links = ('shortid', 'url')
    ordering = ('shortid', 'url', 'views')
    search_fields = ('shortid', 'url')
    readonly_fields = ['shortid', 'views']

admin.site.register(Url, UrlAdmin)
