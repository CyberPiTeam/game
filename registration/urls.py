from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views 

urlpatterns = [
    path('', views.signup, name='game-signup'),
    path('login/', views.signin, name='game-signin'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('', include("django.contrib.auth.urls")),
]