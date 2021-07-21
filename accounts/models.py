from django.db import models
from django.contrib.auth.models import AbstractUser


# Using a custom User model, as suggested by the Django docs:
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_image', blank=True)
