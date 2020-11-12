from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

from account.models import Profile


class RegisterUserForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "first_name", 'class': "form-control input-sm",
                   'placeholder': "Имя"}
        )
    )

    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "last_name", 'class': "form-control input-sm",
                   'placeholder': "Фамилия"}
        )
    )

    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "username", 'class': "form-control input-sm",
                   'placeholder': "Ник Пользователя"}
        )
    )

    email = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "email", 'name': "email", 'class': "form-control input-sm",
                   'placeholder': "Адрес электронной почты"}
        )
    )

    password1 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "password", 'name': "password1", 'class': "form-control input-sm",
                   'placeholder': "Пароль"}
        )
    )

    password2 = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "password", 'name': "password2", 'class': "form-control input-sm",
                   'placeholder': "Подтвердите пароль"}
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя занято!")
        if password1 and password2 and (password1 != password2):
            raise forms.ValidationError("Пароли не совпадают!")
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Веденная почта уже используется!")


class RegisterProfileForm(forms.ModelForm):

    photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('photo',)


class LoginUserForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "username", 'class': "form-control input-sm",
                   'placeholder': "Ник Пользователя"}))

    password = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'type': "password", 'name': "password1", 'class': "form-control input-sm",
                   'placeholder': "Пароль"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not auth.authenticate(username=username, password=password):
            raise forms.ValidationError("Введите правильные ник и пароль!")


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "first_name", 'class': "form-control input-sm",
                   'placeholder': "Имя"}
        )
    )

    last_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "last_name", 'class': "form-control input-sm",
                   'placeholder': "Фамилия"}
        )
    )

    username = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'type': "text", 'name': "username", 'class': "form-control input-sm",
                   'placeholder': "Ник Пользователя"}
        )
    )

    email = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'type': "email", 'name': "email", 'class': "form-control input-sm",
                   'placeholder': "Адрес электронной почты"}
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if username and User.objects.filter(username=username).exclude(username=username).count():
            raise forms.ValidationError("Имя пользователя занято!")
        if email and User.objects.filter(email=email).exclude(email=email).count():
            raise forms.ValidationError("Введенная почта уже используется!")


class EditProfileForm(forms.ModelForm):

    photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('photo', )
