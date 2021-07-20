from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterUserForm


def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    return render(request, 'accounts/profile.html')


def login_view(request):
    register_form = RegisterUserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        messages.error(request, 'Invalid credentials, please try again.')

    return render(
        request,
        'accounts/signin_signup.html',
        {'register_form': register_form},
    )


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}, please log in!'
            )
            return redirect('register')
        else:
            messages.error(request, 'Something went wrong.')

    else:
        register_form = RegisterUserForm()

    return render(
        request,
        'accounts/signin_signup.html',
        {'register_form': register_form},
    )
