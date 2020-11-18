from django.shortcuts import render
from game.models import Player
from django.db import connection
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
import copy
from random import random

from . import challenges as chals
challenges = chals.challenges

# Create your views here.
def start(request):
    return render(request, "game/home.html")

def fruit(request):
    return render(request, "game/pickafruit.html")

@login_required
def challenge(request):
    context = {}
    player = Player.objects.get(username=request.user)
    playerChals = copy.deepcopy(challenges)
    playerSolves = json.loads(player.solves)
    [chal.update(solved=playerSolves.get(chal.get('id')))  for chal in playerChals]
    context['challenges'] = playerChals
    context['fruit'] = player.fruit
    context['score'] = player.score
    context['hat'] = player.hat;
    context['shoes'] = player.shoe;
    context['face'] = player.face;
    return render(request, 'game/challenges.html', context)

