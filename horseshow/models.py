from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from pygraph.classes.graph import graph
from datetime import date, time, datetime, timedelta
from copy import deepcopy

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
    dateStart = models.DateField()
    dateEnd = models.DateField()
    travelTime = models.IntegerField()
    admin = models.ManyToManyField(User)
    hostingBarn = models.ForeignKey('Barn')
    horseShowDays = models.ManyToManyField('HorseShowDay')


def content_file_name(instance, filename):
  return '/'.join(['content', instance.title, filename])

class Barn(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(User,related_name='ownerBarn')
    trainers = models.ManyToManyField(User,related_name='trainerBarn')
    riders = models.ManyToManyField(User,related_name='riderBarn')
    picture = models.ImageField(upload_to=content_file_name);


class Horse(models.Model):
    name = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    height = models.CharField(max_length=5)
    # Fill in rest later

class HorseShowDay(models.Model):
    day = models.IntegerField(default=1)
    rings = models.ManyToManyField('Ring')
    trainers = models.ManyToManyField('Trainer')
    startTime = models.TimeField()

    def organize(self):
        class organizerTimeSlot(object):
            def __init__(self,startTime,endTime):
                self.startTime = startTime
                self.endTime = endTime
                self.values = set()
                self.set = False
                self.rider = None
            def overlaps(self,other):
                return (self.startTime <= other.endTime) and (self.endTime >= other.endTime)

        horseShow = self.horseshow_set.all()[0]
        travelTime = timedelta(minutes=horseShow.travelTime)
        gr = graph()
        timeslots = []
        
        # create time slots for number of riders
        for ring in self.rings.all():
            eventLength = timedelta(minutes=ring.eventLength)
            divisions = ring.divisions.all()
            currentTime = datetime.combine(horseShow.dateStart,
                                           self.horseShowDay.startTime)
            timeslots.append([])
            for division in divisions:
                for rider in division.riders.all():
                    timeslot = organizerTimeSlot(currentTime,
                                                 currentTime+eventLength)
                    timeslot.values = division.riders.all()
                    gr.add_node(timeslot)
                    timeslots[-1].add(timeslot)
                    currentTime += eventLength
        for ring in timeslots:
            for slot in ring:
                for other_ring in timeslots:
                    if other_ring is not ring:
                        for other_slot in other_ring:
                            if slot.overlaps(other_slot):
                                if not gr.has_edge((slot,other_slot)):
                                    gr.add_edge((slot,other_slot))
        print gr

class Ring(models.Model):
    title = models.CharField(max_length=100)
    divisions = models.ManyToManyField('Division')
    eventLength = models.IntegerField(default=20)

class Trainer(models.Model):
    details = models.ForeignKey(User)
    barn = models.ForeignKey(Barn)
    riders = models.ManyToManyField('Rider')

class Rider(models.Model):
    details = models.ForeignKey(User)
    horse = models.ForeignKey(Horse)

class Competitor(models.Model):
    rider = models.ForeignKey('Rider')
    place = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

class Division(models.Model):
    done = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    judge = models.CharField(max_length=100)
    type = models.CharField(choices=DIVISION_TYPES, max_length=20)
    competitors = models.ManyToManyField('Competitor')
