from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Player(models.Model):
	username = models.TextField(primary_key=True)
	solves = models.TextField(null=True,default='{}')
	fruit = models.TextField(null=True,default='')
	body = models.TextField(null=True,default='')
	head = models.TextField(null=True,default='')
	shoe = models.TextField(null=True,default='')
	carry = models.TextField(null=True,default='')
	score = models.IntegerField(null=True,default=0)