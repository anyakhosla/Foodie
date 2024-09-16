from django.urls import path
from . import views

from .views import CustomLoginView


urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('', views.home, name='home'),  # Add your home view if needed
    # ... other URL patterns ...
    path("map", views.mapView, name = "mapView"),
    path('restaurant-data/', views.restaurant_data, name='restaurant_data'),
]


