from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import User
from .forms import RegisterUserForm, UserProfileModelForm


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileModelForm(request.POST, request.FILES)
        if profile_form.is_valid():
            # Get user from database
            user = User.objects.get(username=request.user.username)
            # Update fields
            user.first_name = profile_form.cleaned_data['first_name']
            user.last_name = profile_form.cleaned_data['last_name']
            user.email = profile_form.cleaned_data['email']
            if profile_form.cleaned_data['image']:
                user.image = profile_form.cleaned_data['image']
            if request.POST.get('image-clear'):
                user.image = None
            # Save user
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        # Form not valid
        messages.error(request, 'Something went wrong.')
    # Handle GET request
    user = User.objects.get(username=request.user)
    profile_form = UserProfileModelForm(instance=user)
    return render(
        request, 'accounts/profile.html', {'profile_form': profile_form}
    )


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.delete()
        messages.warning(
            request,
            'Your user profile and all your data have been '
            + 'deleted as you requested.',
        )
        return redirect('home')


def password_reset(request):
    return render(request, 'accounts/password_reset.html')


def send_password_reset_link(request):

    if request.method == 'POST':

        to_address = request.POST.get('recovery-email')

        subject = 'Your password reset link for Timelinor'
        message = ''
        from_address = settings.DEFAULT_FROM_EMAIL
        to_addresses = [to_address]

        smtp_response = send_mail(
            subject,
            message,
            from_address,
            to_addresses,
            fail_silently=False,
        )
        if smtp_response == 1:
            messages.success(request, 'Mail sent!')
        else:
            messages.error(
                request, f'Mail not sent, return code {smtp_response}'
            )

        return redirect('home')


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

        # Form invalid
        messages.error(request, 'Something went wrong, see fields below.')

    else:
        register_form = RegisterUserForm()

    return render(
        request,
        'accounts/signin_signup.html',
        {'register_form': register_form},
    )
