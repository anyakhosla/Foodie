from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

# from .models import Question, Choice

def mapView(request):
    # question = get_object_or_404(Question, pk=id)
    # return render(request, "foodie/mapView.html", {"question": question})
    return render(request, "foodie/mapView.html")
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
