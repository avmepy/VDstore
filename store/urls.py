from django.urls import path
from . import views
from .views import ShowCategory
from .models import Product

app_name = "store"


urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.my_cart, name="my_cart"),
    path('category/<str:product>/', ShowCategory.as_view(), name="show_category"),
    path('<int:product_id>/', views.product_detail, name="product_detail_url"),
    path('<int:product_id>/add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('<int:product_id>/add_comment/', views.create_comment, name="add_comment_url"),
]