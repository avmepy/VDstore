from django.urls import path
from . import views
from .views import ShowCategory
from .models import Product

app_name = "store"


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:slug>/', views.product_detail, name="product_detail_url"),
    path('category/<str:product>', ShowCategory.as_view(), name="show_category"),
    path('<slug:slug>/added_to_cart', views.add_to_cart, name="add_to_cart"),
    path('cart', views.my_cart, name="my_cart"),
]

