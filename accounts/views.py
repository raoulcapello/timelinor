from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from .models import User


def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    return render(request, 'accounts/profile.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return render(
                request,
                'accounts/signin_signup.html',
                {'message_warning': 'Invalid credentials, please try again.'},
            )

    return render(request, 'accounts/signin_signup.html')


def logout_view(request):
    logout(request)
    return render(
        request,
        'timelinor/home.html',
        {'message_success': 'You have been logged out.'},
    )


def register(request):
    pass
