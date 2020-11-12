from django.contrib import messages
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

            user = auth.authenticate(request, username=user.username, password=user.password)
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



@login_required
def profile_detail(request):

    user = request.user

    context = {
        'user': user
    }

    return render(request, 'account/profile_detail.html', context=context)

