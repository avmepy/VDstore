from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:product>', views.show_category, name="show_category"),
    path('<str:slug>', views.product_detail, name="product_detail_url"),
]

