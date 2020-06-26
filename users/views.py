from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Document
from django.contrib.auth import update_session_auth_hash


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'mysite/home.html', context={'login': 'Authenticated successfully'})
                else:
                    return render(request, 'mysite/home.html', context={'login': 'Disabled account'})
            else:
                return render(request, 'users/login.html', context={'form': form, 'login': 'Invalid login or password'})

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'mysite/home.html')


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


def check_password(first_password, second_password):
    if first_password == second_password:
        return True
    else:
        return False


@login_required
def a_change_password(request):
    user = User.objects.get(username=request.user)
    print(user)
    print(request.method)
    if request.method != 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'users/password_change_form.html',
                  {'form': form, 'user': user,'pass_change':'Your password has been successfully changed '})
        else:
            return render(request, 'users/password_change_form.html',
                          {'form': form, 'user': user, 'pass_change': 'Your password has not been  changed '})
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/password_change_form.html',
                  {'form': form, 'user': user})


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']


def user_files(request):
    if request.user.is_authenticated == True:
        files = []
        file = Document.objects.all()
        for doc in file:
            if doc.owner == request.user:
                files.append(doc)
        return render(request, 'users/account.html', {'files': files})
