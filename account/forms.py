from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class RegisterUserForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "first_name", 'class': "form-control input-sm", 'placeholder': "Имя"}))

    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "last_name", 'class': "form-control input-sm", 'placeholder': "Фамилия"}))

    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "username", 'class': "form-control input-sm", 'placeholder': "Имя пользователя"}))

    email = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "email", 'name': "email", 'class': "form-control input-sm", 'placeholder': "Адрес электронной почты"}))

    password1 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "password", 'name': "password1", 'class': "form-control input-sm",
                   'placeholder': "Пароль"}))

    password2 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "password", 'name': "password2", 'class': "form-control input-sm",
                   'placeholder': "Подтвердите пароль"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if username and email and password1 and password2:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Имя пользователя занято!")
            if password1 != password2:
                raise forms.ValidationError("Пароли не совпадают!")


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)