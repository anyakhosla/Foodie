from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Restaurant, CustomUser
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

def mapView(request):
    # question = get_object_or_404(Question, pk=id)
    # return render(request, "foodie/mapView.html", {"question": question})
    return render(request, "foodie/mapView.html", {'GOOGLE_MAPS_API_KEY' : settings.GOOGLE_MAPS_API_KEY})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f'Account created for {user.username}!')
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# myapp/views.py

# class CustomLoginView(LoginView):
#     template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('foodie:mapView')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('foodie:login')

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
            'overall_rating': restaurant.overall_rating,
            'id': restaurant.id,
            'phone_number': restaurant.phone_number,
            'website': restaurant.website
        })

    return JsonResponse({'restaurants': restaurant_list})


from django.http import JsonResponse
from .models import Restaurant
import math


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 3958.8  # Radius of the Earth in miles
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Distance in miles
    return distance


def filter_restaurants(request):
    min_rating = float(request.GET.get('min_rating', 1))
    max_distance = float(request.GET.get('max_distance', 20))
    query = request.GET.get('q', '').strip()

    # Center of Atlanta
    center_lat = 33.7490
    center_lon = -84.3880

    restaurants = Restaurant.objects.all()

    # Apply search query filter
    if query:
        restaurants = restaurants.filter(Q(name__icontains=query) | Q(cuisine__icontains=query))

    filtered_restaurants = []

    for restaurant in restaurants:
        distance = calculate_distance(center_lat, center_lon, restaurant.latitude, restaurant.longitude)

        if restaurant.overall_rating >= min_rating and distance <= max_distance:
            filtered_restaurants.append({
                'name': restaurant.name,
                'cuisine': restaurant.cuisine,
                'address': restaurant.address,
                'latitude': restaurant.latitude,
                'longitude': restaurant.longitude,
                'overall_rating': restaurant.overall_rating,
                'id': restaurant.id,
                'phone_number': restaurant.phone_number,
                'website': restaurant.website,
                'distance': round(distance, 2)  # Include the distance in the response
            })

    return JsonResponse({'restaurants': filtered_restaurants})


def restaurant_list(request):
    query = request.GET.get('q', '')
    if query:
        restaurants = Restaurant.objects.filter(Q(name__icontains=query) | Q(cuisine__icontains=query))
    else:
        restaurants = Restaurant.objects.all()

    context = {
        'restaurants': restaurants,
        'query': query,
    }
    return render(request, 'foodie/restaurant_list.html', context)

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    reviews = restaurant.reviews if restaurant.reviews else []
    context = {
        'restaurant': restaurant,
        'reviews': reviews,
    }
    return render(request, 'foodie/restaurant_detail.html', context)

def user_profile_page(request): # add user id parameter
    # add logic to check if user is signed in
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser, pk=request.user.id)
        context = {
            'user': user,
        }
        return render(request, "foodie/userPage.html", context) # return render(request, "foodie/userPage.html", {'user_id' : user_id})
    else:
        return redirect('foodie:login')