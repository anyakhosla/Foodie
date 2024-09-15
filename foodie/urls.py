from django.urls import path
from . import views

app_name = 'foodie'

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
]
