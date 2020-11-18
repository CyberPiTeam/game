from django.urls import path, include
from . import views 
from . import logic

urlpatterns = [
    path('home/', views.start, name='entergame'),
    path('challenges/', views.challenge, name='pickchallenge'),
    path('pickafruit/', views.fruit, name='pickfruit'),
    path('submitchal/', logic.submitChal, name='submitchal'),
    path('setfruit/', logic.setFruit, name='setFruit'),
    path('chooseprize/', logic.choosePrize, name='choosePrize')
]
