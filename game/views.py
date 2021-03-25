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
from . import bonus_challenges as bchals
challenges = chals.challenges
bonus_challenges=bchals.challenges
# Create your views here.
def start(request):
    return render(request, "game/home.html")

def aboutteam(request):
    return render(request, "game/about.html")

def fruit(request):
    context = {}
    try:
        player = Player.objects.get(username=request.user)
    except Player.DoesNotExist:
        player = Player.objects.create(username=request.user)
    context['fruit'] = player.fruit
    return render(request, "game/pickafruit.html", context)


def challenge(request):
    context = {}
    try:
        player = Player.objects.get(username=request.user)
    except Player.DoesNotExist:
        player = Player.objects.create(username=request.user)
    playerChals = copy.deepcopy(challenges)
    playerSolves = json.loads(player.solves)
    [chal.update(solved=playerSolves.get(chal.get('id')))  for chal in playerChals]
    context['challenges'] = playerChals
    context['fruit'] = player.fruit
    context['score'] = player.score
    context['head'] = player.head
    context['eyes'] = player.eyes
    context['nose'] = player.nose 
    context['mouth'] = player.mouth
    context['carry'] = player.carry
    return render(request, 'game/challenges.html', context)
    
    
    
def bonus_challenge(request):
    context = {}
    try:
        player = Player.objects.get(username=request.user)
    except Player.DoesNotExist:
        player = Player.objects.create(username=request.user)
    playerChals = copy.deepcopy(bonus_challenges)
    playerSolves = json.loads(player.solves)
    [bchal.update(solved=playerSolves.get(bchal.get('id')))  for bchal in playerChals]
    context['challenges'] = playerChals
    context['fruit'] = player.fruit
    context['score'] = player.score
    context['head'] = player.head
    context['eyes'] = player.eyes
    context['nose'] = player.nose 
    context['mouth'] = player.mouth
    context['carry'] = player.carry
    return render(request, 'game/bonus_challenges.html', context)


def bonus_challenge(request):
    context = {}
    try:
        player = Player.objects.get(username=request.user)
    except Player.DoesNotExist:
        player = Player.objects.create(username=request.user)
    playerChals = copy.deepcopy(bonus_challenges)
    playerSolves = json.loads(player.solves)
    [bchal.update(solved=playerSolves.get(bchal.get('id')))  for bchal in playerChals]
    context['challenges'] = playerChals
    context['fruit'] = player.fruit
    context['score'] = player.score
    context['head'] = player.head
    context['eyes'] = player.eyes
    context['nose'] = player.nose 
    context['mouth'] = player.mouth
    context['carry'] = player.carry
    return render(request, 'game/bonus_challenges.html', context)

