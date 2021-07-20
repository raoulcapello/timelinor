from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to all visible fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
