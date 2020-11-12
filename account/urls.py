from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', profile_detail, name='profile_detail_url'),
    path('register/', profile_register, name='profile_register_url'),
    path('login/', profile_login, name='profile_login_url'),
    path('logout/', profile_logout, name='profile_logout_url'),
    path('edit/', profile_edit, name='profile_edit_url'),
    path('change_password/', profile_change_password, name='profile_change_password_url'),

]
