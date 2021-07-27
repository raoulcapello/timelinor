from django.db import models

from accounts.models import User


class Timeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

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
