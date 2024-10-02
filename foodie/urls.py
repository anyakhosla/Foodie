from django.urls import path
from . import views
from django.urls import path, include
from django.shortcuts import get_object_or_404

app_name = 'foodie'
from .views import CustomLoginView
from .views import register, login_view, logout_view, mapView

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    #path('', views.home, name='home'),  # Add your home view if needed
    path("map/", views.mapView, name = "mapView"),
    path('map/restaurant-data/', views.restaurant_data, name='restaurant_data'),
    path('restaurant/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
    path('filter_restaurants/', views.filter_restaurants, name='filter_restaurants'),
    path('user/', views.user_profile_page, name='user_profile_page'),
    path('restaurant/<int:restaurant_id>/add_favorite/', views.add_restaurant_favorite, name='add_restaurant_favorite'),
    path('restaurant/<int:restaurant_id>/<str:destination>/remove_favorite/', views.remove_restaurant_favorite, name='remove_restaurant_favorite')
]


