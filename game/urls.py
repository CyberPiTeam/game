from django.urls import path, include
from . import views 
from . import logic

urlpatterns = [
    path('home/', views.start, name='entergame'),
    path('challenges/', views.challenge, name='pickchallenge'),
    path('pickafruit/', views.fruit, name='pickfruit'),
    path('about/', views.aboutteam, name="aboutpage"),
    path('submitchal/', logic.submitChal, name='submitchal'),
    path('bsubmitchal/', logic.bsubmitChal, name='bsubmitchal'),
    path('setfruit/', logic.setFruit, name='setFruit'),
    path('chooseprize/', logic.choosePrize, name='choosePrize'),
    path('resetgame/', logic.resetgame, name='resetgame'),
    path('bonus_challenges/', views.bonus_challenge, name='bonus_challenge')
]
