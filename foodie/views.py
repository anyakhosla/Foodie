from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

# from .models import Question, Choice

def mapView(request):
    # question = get_object_or_404(Question, pk=id)
    # return render(request, "foodie/mapView.html", {"question": question})
    return render(request, "foodie/mapView.html", {'GOOGLE_MAPS_API_KEY' : settings.GOOGLE_MAPS_API_KEY})
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

from django.http import JsonResponse
from .models import Restaurant

def restaurant_data(request):
    restaurants = Restaurant.objects.all()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_list.append({
            'name': restaurant.name,
            'cuisine': restaurant.cuisine,
            'address': restaurant.address,
            'latitude': restaurant.latitude,
            'longitude': restaurant.longitude,
            'overall_rating': restaurant.overall_rating
        })
    return JsonResponse({'restaurants': restaurant_list})
