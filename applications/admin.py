# -*- coding: utf-8 -*-

from django.contrib import admin

from applications.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    fields = ('name', 'thumb_url', 'web_hook', 'channel')
