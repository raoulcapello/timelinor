from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

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
                {'warning_message': 'Invalid credentials, please try again.'},
            )

    return render(request, 'accounts/signin_signup.html')


def logout_view(request):
    logout(request)
    return render(
        request,
        'timelinor/home.html',
        {'success_message': 'You have been logged out.'},
    )


def register(request):
    if request.method == 'POST':
        # Get user data
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Check if passwords match
        if password != password2:
            return render(
                request,
                'accounts/signin_signup.html',
                {'warning_message': 'Passwords don\'t match.'},
            )

        # Create user, will fail if username exists
        try:
            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        except IntegrityError:
            return render(
                request,
                'accounts/signin_signup.html',
                {'warning_message': 'Username unavailable.'},
            )

        return render(
            request,
            'accounts/signin_signup.html',
            {'message_success': 'Account created, please log in.'},
        )
