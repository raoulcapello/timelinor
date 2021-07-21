from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (('User Profile Settings', {'fields': ('image',)}),)

admin.site.register(User, UserAdmin)
