from django.urls import path
from . import views
from .views import ShowCategory

app_name = "store"


urlpatterns = [
    path('', views.home, name="home"),
    path('<str:slug>/', views.product_detail, name="product_detail_url"),
    path('category/<str:product>', ShowCategory.as_view(), name="show_category"),
]

