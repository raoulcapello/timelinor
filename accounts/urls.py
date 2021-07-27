from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('delete-profile', views.delete_profile, name='delete-profile'),
    # Password reset via profile
    path(
        'logged_in_password_reset',
        views.logged_in_password_reset,
        name='logged_in_password_reset',
    ),
    # Password reset procedure via email link
    path('password_reset', views.password_reset, name='password_reset'),
    path(
        'password_reset/done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
]
