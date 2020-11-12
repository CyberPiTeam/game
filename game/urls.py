from django.urls import path, include
from . import views 

urlpatterns = [
    path('home/', views.start, name='entergame'),
    path('challenges/', views.challenge, name='pickchallenge'),
    path('pickafruit/', views.fruit, name='pickfruit')
]