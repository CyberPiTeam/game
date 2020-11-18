from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
#class customFruit(models.Model):
#	username = models.ForeignKey(User, on_delete=models.CASCADE,default=None,blank=True)
#	fruit = models.TextField(null=True)
#	face = models.TextField(null=True)
#	hat = models.TextField(null=True)
#	shoes = models.TextField(null=True)
#	sunglasses = models.TextField(null=True)
#	tools = models.TextField(null=True)
#	wig = models.TextField(null=True) 
#	completed = models.TextField(null=True)


class Player(models.Model):
	fruit = models.TextField(null=True)
	username = models.TextField(primary_key=True)
	solves = models.TextField(null=True,default='{}')
	fruit = models.TextField(null=True,default='')
	face = models.TextField(null=True,default='')
	hat = models.TextField(null=True,default='')
	shoe = models.TextField(null=True,default='')
	sunglasses = models.TextField(null=True,default='')
	tools = models.TextField(null=True,default='')
	wig = models.TextField(null=True,default='') 
	score = models.IntegerField(null=True,default=0) 


# I need to store the username, avatar, array of finished challenges
# https://stackoverflow.com/questions/1110153/what-is-the-most-efficient-way-to-store-a-list-in-the-django-models


#test = Test()
#print (test.testvalue)
#test.testvalue="hi"
#test.save()
#print (test.testvalue)
