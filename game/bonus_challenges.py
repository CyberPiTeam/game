import json
from . import prizes
challenges = json.loads(open("bonus_challenges.json","r").read())
#generate an id for each challenge based on name
[chal.update(id =str(chal.get('name')).encode("utf-8").hex(),prizes=[])  for chal in challenges]

for i in range(0,len(prizes.prizes)):
    challenges[i%len(challenges)].get('prizes').append(prizes.prizes[i])


def findChal(id):
    return next(chal for chal in challenges if chal.get('id')==id)

def findPrize(id):
    return next(prize for prize in prizes.prizes if prize.get('id')==id)
