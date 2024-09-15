from django.shortcuts import render, get_object_or_404
from .models import Restaurant

def restaurant_detail(request, restaurant_id):
    # Fetch the restaurant by ID
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    # Fetching the reviews from the JSONField (assuming the reviews are stored in a list)
    reviews = restaurant.reviews if restaurant.reviews else []

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
    }
    return render(request, 'restaurant_detail.html', context)

def restaurant_list(request):
    restaurants = Restaurant.objects.all() # do not change name of this variable

    context = {}
    context['restaurants'] = restaurants

    return render(request, 'restaurant_list.html', context)