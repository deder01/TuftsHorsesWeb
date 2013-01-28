from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

DIVISION_TYPES = (
	("openFences","Open Fences"),
	("interFences","Intermediate Fences"),
	("noviceFences","Novice Fences"),
	("openFlat","Open Flat"),
	("interFlat","Intermediate Flat"),
	("noviceFlat","Novice Flat"),
	("wtcAdv","Advanced Walk Trot Cantor"),
	("wtcBegin","Beginner Walk Trot Cantor"),
	("walkTrot","Walk Trot"),
)

class HorseShow(models.Model):
	location = models.CharField(max_length=400)
	title = models.CharField(max_length=100)
	dateStart = models.DateTimeField()
	dateEnd = models.DateTimeField()
	travelTime = models.IntegerField()
	admin = models.ManyToManyField(User)
	hostingBarn = models.ForeignKey('Barn')
	horseShowDays = models.ManyToManyField('HorseShowDay')

class Barn(models.Model):
	title = models.CharField(max_length=100)
	location = models.CharField(max_length=200)
	owner = models.ForeignKey(User,related_name='ownerBarn')
	trainers = models.ManyToManyField(User,related_name='trainerBarn')
	riders = models.ManyToManyField(User,related_name='riderBarn')

class Horse(models.Model):
	name = models.CharField(max_length=100)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	height = models.CharField(max_length=5)
	# Fill in rest later

class HorseShowDay(models.Model):
	rings = models.ManyToManyField('Ring')
	trainers = models.ManyToManyField('Trainer')

class Ring(models.Model):
	title = models.CharField(max_length=100)
	divisions = models.ManyToManyField('Division')

class Trainer(models.Model):
	details = models.ForeignKey(User)
	barn = models.ForeignKey(Barn)
	riders = models.ManyToManyField('Rider')

class Rider(models.Model):
	details = models.ForeignKey(User)
	horse = models.ForeignKey(Horse)

class Division(models.Model):
	title = models.CharField(max_length=100)
	judge = models.CharField(max_length=100)
	type = models.CharField(choices=DIVISION_TYPES, max_length=20)
	riders = models.ManyToManyField(Rider)






