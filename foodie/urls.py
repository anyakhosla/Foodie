from django.urls import path
from . import views
from django.urls import path, include

from .views import CustomLoginView
from .views import register, login_view, logout_view, mapView

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('map/', views.mapView, name = "mapView"),
    path('restaurant-data/', views.restaurant_data, name='restaurant_data'),
]


