from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from .forms import LoginForm, UserRegistrationForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    return render(request, 'users/login.html', context={'login': 'Authenticated successfully'})
                else:
                    return render(request, 'users/login.html', context={'login': 'Disabled account'})
            else:
                return render(request, 'users/login.html', context={'form': form, 'login': 'Invalid login or password'})
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return (request,'registration.logged_out.html')


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})