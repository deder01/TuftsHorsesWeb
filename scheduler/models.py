from django.db import models
from horseshow.models import Rider

class Schedule(models.Model):
    length = models.IntegerField()
    breakLength = models.IntegerField()
    timeSlots = models.ManyToManyField('TimeSlot')


class TimeSlot(models.Model):
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	riders = models.ManyToManyField(Rider)
