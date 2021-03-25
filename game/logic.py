from django.views.decorators.csrf import csrf_exempt
from game.models import Player
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from . import challenges as chals
from . import bonus_challenges as bchals
from . import prizes
challenges = chals.challenges

@csrf_exempt
def submitChal(request):
    body = json.loads(request.body)
    answer = chals.findChal(body.get('id'))
    if answer.get('flag') == body.get('flag'):
        player = Player.objects.get(username=request.user)
        playerChals = json.loads(player.solves)
        solved = playerChals.get(answer.get('id'))
        if solved:
            pass
        else:
            playerChals[answer.get('id')] = True
            player.score = player.score + int(answer.get('points'))
            player.solves = json.dumps(playerChals)
            player.save()
        #need to add some sort of item to a db for the user that shows we have a decision to make and also mark this challenge complete
        return JsonResponse({
                "success":True,
                "prizes":answer.get('prizes')
            })
    else:
        return JsonResponse({
                "success":False
            })
#bonus challenges submit
@csrf_exempt
def bsubmitChal(request):
    body = json.loads(request.body)
    answer = bchals.findChal(body.get('id'))
    if answer.get('flag') == body.get('flag'):
        player = Player.objects.get(username=request.user)
        playerChals = json.loads(player.solves)
        solved = playerChals.get(answer.get('id'))
        if solved:
            pass;
        else:
            playerChals[answer.get('id')] = True;
            player.score = player.score + int(answer.get('points'))
            player.solves = json.dumps(playerChals)
            player.save()
        #need to add some sort of item to a db for the user that shows we have a decision to make and also mark this challenge complete
        return JsonResponse({
                "success":True,
                "prizes":answer.get('prizes')
            })
    else:
        return JsonResponse({
                "success":False
            })
@csrf_exempt
def setFruit(request):
    body = json.loads(request.body)
    try:
        player = Player.objects.get(username=request.user)
        player.fruit = body.get('fruit')
    except:
        player = Player.objects.create(fruit=body.get('fruit'),username=request.user)
    player.save()
    return JsonResponse({
            "success":True
        })

@csrf_exempt
def choosePrize(request):
    body = json.loads(request.body)
    player = Player.objects.get(username=request.user)
    playerSolves = json.loads(player.solves)
    if playerSolves.get(body.get('challengeId')):
        prize = chals.findPrize(body.get('id'))
        if prize is None:
            return JsonResponse({
                    "success":False
                })
        #player[prize.get('type')] = prize.get('url')
        setattr(player,prize.get('type'),prize.get('url'))
        player.save()
        return JsonResponse({
                "success":True
            })
    else:
        return JsonResponse({
                "success":False
            })

@csrf_exempt
def resetgame(request):
    body = json.loads(request.body)
    password = body.get("enteredpassword")
    user = User.objects.get(username=request.user)
    if user.check_password(password):
        player = Player.objects.get(username=request.user)
        player.solves = '{}'
        player.eyes = ''
        player.head = ''
        player.nose = ''
        player.mouth = ''
        player.carry = ''
        player.score = 0
        player.save()
        return JsonResponse({
            "success":True
        })  
    else:
        return JsonResponse({
                "success":False
            })