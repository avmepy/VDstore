from django.urls import path
from . import views

app_name = "store"


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:product_id>/', views.product_detail, name="product_detail_url"),
    path('<int:product_id>/add_comment/', views.create_comment, name="add_comment_url"),
    path('category/<str:product>/', views.show_category, name="show_category"),
]

