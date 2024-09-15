from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path("map", views.mapView, name = "mapView"),
    path('profile/', views.profile_view, name='profile'),
]
