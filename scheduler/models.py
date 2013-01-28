from django.db import models
from horseshow.models import Rider, Ring

class Schedule(models.Model):
    length = models.IntegerField()
    breakLength = models.IntegerField()
    timeSlots = models.ManyToManyField('TimeSlot')
    ring = models.OneToOneField(Ring)


class TimeSlot(models.Model):
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	riders = models.ManyToManyField(Rider)
