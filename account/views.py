from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import  auth

from .models import Profile
from .forms import *


def profile_register(request):

    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = User.objects.create_user(username=user_form.cleaned_data.get('username'),
                                            first_name=user_form.cleaned_data.get('first_name'),
                                            last_name=user_form.cleaned_data.get('last_name'),
                                            password=user_form.cleaned_data.get('password1'),
                                            email=user_form.cleaned_data.get('email'),
                                            )
            user.profile.photo = profile_form.cleaned_data.get('photo')
            user.save()

            messages.success(request, 'Регистрация прошла успешно!')

            user = auth.authenticate(username=user_form.cleaned_data.get('username'),
                                     password=user_form.cleaned_data.get('password1'))

            auth.login(request, user)

            return redirect('profile_detail_url')
    else:
        user_form = RegisterUserForm()
        profile_form = RegisterProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'account/profile_register.html', context=context)


def profile_login(request):

    if request.method == 'POST':

        form = LoginUserForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))

            auth.login(request, user)
            return redirect('profile_detail_url')
    else:

        form = LoginUserForm()

    context = {
        'form': form
    }

    return render(request, 'account/profile_login.html', context=context)


@login_required
def profile_logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile_edit(request):

    if request.method == 'POST':

        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():

            # login_password_after_edit = request.user.password
            user = user_form.save()
            profile_form.save()

            update_session_auth_hash(request, user)
            messages.success(request, "Данные профиля успешно изменены!")

            return redirect('profile_detail_url')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'account/profile_edit.html', context=context)


@login_required
def profile_change_password(request):

    user = request.user

    if request.method == 'POST':
        form = ChangePasswordUserForm(data=request.POST, request=request)
        if form.is_valid():

            user.set_password(form.cleaned_data.get('password2'))
            user.save()

            update_session_auth_hash(request, user)
            messages.success(request, "Данные профиля успешно изменены!")

            return redirect('profile_detail_url')
    else:
        form = ChangePasswordUserForm(request=request)

    context = {
        'form': form
    }

    return render(request, 'account/profile_change_password.html', context=context)


@login_required
def profile_detail(request):

    user = request.user

    context = {
        'user': user
    }

    return render(request, 'account/profile_detail.html', context=context)

