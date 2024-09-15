from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('profile/', views.profile_view, name='profile'),
]
