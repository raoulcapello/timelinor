from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from .models import User
from .forms import (
    RegisterUserForm,
    UserProfileModelForm,
    LoggedInPasswordResetForm,
    CustomPasswordResetForm,
)


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
    password_reset_form = LoggedInPasswordResetForm()

    return render(
        request,
        'accounts/profile.html',
        {
            'profile_form': profile_form,
            'password_reset_form': password_reset_form,
        },
    )


@login_required
def logged_in_password_reset(request):
    """
    Enables a logged in user to reset their password via their profile page.
    """
    if request.method == 'POST':
        password_reset_form = LoggedInPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            user = User.objects.get(username=request.user.username)
            current_password = password_reset_form.cleaned_data[
                'current_password'
            ]
            new_password1 = password_reset_form.cleaned_data['new_password1']
            new_password2 = password_reset_form.cleaned_data['new_password2']
            if not user.check_password(current_password):
                messages.error(request, 'Wrong password, please try again.')
                return redirect('profile')
            if not new_password1 == new_password2:
                messages.error(
                    request, 'Passwords don\'t match, please try again.'
                )
                return redirect('profile')

            # Valid current password, and matching new passwords
            # Go ahead and change password to the new password
            user.set_password(new_password1)
            user.save()
            messages.success(request, 'Password updated.')

        else:
            print(password_reset_form.errors)
            messages.error(
                request, 'Passwords didn\'t match, please try again.'
            )

        return redirect('profile')


@login_required
def delete_profile(request):
    """
    Enables a logged in user to permanently delete all their personal data.
    """
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
    """
    Allows any user to reset their password via the password email reset
    procedure, without needing to log in.

    Step 1 in the password email reset procedure.

    Based on the patterns in this article by Jaysha:
    https://www.ordinarycoders.com/blog/article/django-password-reset
    """
    if request.method == 'POST':
        password_reset_form = CustomPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'accounts/password_reset_email.txt'
                    email_context = {
                        'email': user.email,
                        'domain': request.get_host(),
                        'site_name': 'Timelinor',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': settings.SITE_PROTOCOL,
                    }
                    email = render_to_string(
                        email_template_name, email_context
                    )
                    try:
                        send_mail(
                            subject,
                            email,
                            'noreply@timelinor.com',
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

            # For security reasons, always redirect users to the success
            # page, to prevent probing of email addresses on file in our
            # database.
            return redirect('password_reset_done')

    password_reset_form = CustomPasswordResetForm()

    return render(
        request,
        'accounts/password_reset.html',
        {'password_reset_form': password_reset_form},
    )


def send_password_reset_link(request):
    """
    Step 2 in the password email reset procedure.
    """
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
