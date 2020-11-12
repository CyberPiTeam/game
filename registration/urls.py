from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.signup, name='game-signup'),
    path('', include("django.contrib.auth.urls")),
]