from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('delete-profile', views.delete_profile, name='delete-profile'),
]
