# -*- coding: utf-8 -*-

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Application(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='')
    channel = models.CharField(max_length=100, blank=False, default='')
    thumb_url = models.CharField(max_length=256, blank=False, default='')
    web_hook = models.CharField(max_length=256, blank=False, default='')

    def __str__(self):
        return self.name
