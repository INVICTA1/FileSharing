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
                    return render(request, 'mysite/home.html', context={'login': 'Authenticated successfully','form': form})
            else:
                return render(request, 'users/login.html', context={'login': 'Invalid login or password','form': form},)
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})



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
def user_logout(request):
    logout(request)
    return render(request, 'mysite/home.html')


@login_required
def a_change_password(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'users/password_change_form.html',
                          {'form': form, 'user': user, 'pass_change': 'Your password has been successfully changed '})
        else:
            return render(request, 'users/password_change_form.html',
                          {'form': form, 'user': user, 'pass_change': 'Your password has not been  changed '})
    else:
        form = PasswordChangeForm(user=request.user)
        print(form)

    return render(request, 'users/password_change_form.html',
                  {'form': form, 'user': user})

@login_required
def user_files(request):
    if request.user.is_authenticated == True:
        files = []
        file = Document.objects.all()
        for doc in file:
            if doc.owner == request.user:
                files.append(doc)
        return render(request, 'users/account.html', {'files': files})

@login_required
def del_user_files(request,name):
    if request.user.is_authenticated == True:
        documents = Document.objects.all()
        for doc in documents:
            if doc.name == name:
                doc.delete()
        return user_files(request)



