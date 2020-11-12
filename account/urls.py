from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', profile_detail, name='profile_detail_url'),

]
