from django.shortcuts import render

from accounts.forms import RegisterUserForm


def home(request):
    register_form = RegisterUserForm()
    return render(
        request, 'timelinor/home.html', {'register_form': register_form}
    )
