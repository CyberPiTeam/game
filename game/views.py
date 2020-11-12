from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, "game/home.html")

def fruit(request):
    return render(request, "game/pickafruit.html")

def challenge(request):
    return render(request, "game/challenges.html")