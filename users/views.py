from django.shortcuts import render
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'base.html')


def register(request):
    """register new user"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            return render(request, 'registration/registration_complete.html', {'user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
