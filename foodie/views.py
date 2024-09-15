from django.shortcuts import render, get_object_or_404

# Create your views here.

# from .models import Question, Choice

def mapView(request, id):
    # question = get_object_or_404(Question, pk=id)
    # return render(request, "foodie/mapView.html", {"question": question})
    return render(request, "foodie/mapView.html")
