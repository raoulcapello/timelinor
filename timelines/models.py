from django.db import models
from django.utils.text import slugify

from accounts.models import User


class Timeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    # Based on:
    # https://kodnito.com/posts/slugify-urls-django/
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TimelineEvent(models.Model):
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: {self.subtitle} ({self.timeline})'
