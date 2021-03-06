from django.conf import settings
from django.db import models
from django.utils.text import slugify

import string
import random


def get_random_slug():
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(6)
    )


class Timeline(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    button = models.BooleanField(default=False)
    button_text = models.CharField(max_length=50, default='Back')
    button_url = models.URLField(default='', blank=True)

    # Based on:
    # https://kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_slug() + '-' + self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TimelineEvent(models.Model):
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.title}: {self.subtitle} ({self.timeline})'
