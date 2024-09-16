from django.shortcuts import render, get_object_or_404
from .models import Restaurant

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.views import LoginView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

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
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'


def mapView(request):
    # question = get_object_or_404(Question, pk=id)
    # return render(request, "foodie/mapView.html", {"question": question})
    return render(request, "foodie/mapView.html", {'GOOGLE_MAPS_API_KEY' : settings.GOOGLE_MAPS_API_KEY})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Additional logic...
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
                return redirect('home')
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
    return redirect('login')


def home(request):
    return render(request, 'home.html')


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

def restaurant_list(request):
    restaurants = Restaurant.objects.all()  # do not change name of this variable

    context = {}
    context['restaurants'] = restaurants

    return render(request, 'foodie/restaurant_list.html', context)


def restaurant_detail(request, restaurant_id):
    # Fetch the restaurant by ID
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    # Fetching the reviews from the JSONField (assuming the reviews are stored in a list)
    reviews = restaurant.reviews if restaurant.reviews else []

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
    }
    return render(request, 'foodie/restaurant_detail.html', context)
