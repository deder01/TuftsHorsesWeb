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
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=400)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    admin = models.ManyToManyField(User)
    hostingTeam = models.ForeignKey('Team',null=True)
    divisions = models.ManyToManyField('Division')
    teams = models.ManyToManyField('ShowTeam')
    maxriders = models.IntegerField(default=15)

class Team(models.Model):
    school = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=200)
    captains = models.ManyToManyField(User,related_name='captainTeam')
    trainers = models.ManyToManyField(User,related_name='trainerTeam')
    riders = models.ManyToManyField(User,related_name='riderTeam')

class Horse(models.Model):
    name = models.CharField(max_length=100,default="")
    height = models.CharField(max_length=5,default="")
    weight = models.CharField(max_length=10,default="1000")
    gender = models.CharField(max_length=20,default="gelding")
    
"""class HorseShowDay(models.Model):
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
"""

class ShowTeam(models.Model):
    team = models.ForeignKey(Team)
    riders = models.ManyToManyField('Rider')
    trainers = models.ManyToManyField(User)
    def points(self):
        pass

class Rider(models.Model):
    details = models.ForeignKey(User)
    horse = models.ForeignKey(Horse)
    place = models.IntegerField(default=-1)
    pointed = models.BooleanField(default=True)

class Division(models.Model):
    title = models.CharField(max_length=100)
    judge = models.CharField(max_length=100)
    type = models.CharField(choices=DIVISION_TYPES, max_length=20)
    order = models.IntegerField(default=-1)
    eventLength = models.IntegerField(default=10)
    horses = models.ManyToManyField(Horse,through='Membership')
    riders = models.ManyToManyField(Rider)

class Membership(models.Model):
    horse = models.ForeignKey(Horse)
    division = models.ForeignKey(Division)
    alternate = models.BooleanField(default=False)
    able = models.BooleanField(default=True) 
    height_limit = models.IntegerField(default=300) #inches
    weight_limit = models.IntegerField(default=300) #pounds

