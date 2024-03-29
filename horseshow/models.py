from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from pygraph.classes.graph import graph
from datetime import date, time, datetime, timedelta
from copy import deepcopy
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from uuid import uuid1

DIVISION_TYPES = (
    ("none","None"),
    ("open","Open"),
    ("intermediate","Intermediate"),
    ("novice","Novice"),
    ("wtc","Walk Trot Cantor"),
    ("wt","Walk Trot")
)

CLASS_TYPES = (
    ("flat","Flat"),
    ("fences","Fences")
)

class Profile(models.Model):
    user = models.OneToOneField(User)
    is_rider = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_region_director = models.BooleanField(default=False)
    is_zone_director = models.BooleanField(default=False)

    # rider properties
    fences_division = models.CharField(max_length=20,choices=DIVISION_TYPES[:4],default="none")
    flat_division = models.CharField(max_length=20,choices=DIVISION_TYPES,default="none")
    points = models.IntegerField(default=0)

class HorseShowManager(models.Manager):
    def create(self,*args,**kwargs):
        new_horse_show = super(HorseShowManager,self).create(*args,**kwargs)
        new_horse_show.save()
        team = new_horse_show.hosting_team
        for regional_team in Team.objects.filter(region=team.region):
            new_show_team = ShowTeam.objects.create(team=regional_team)
            new_show_team.save()
            new_horse_show.teams.add(new_show_team)
            for trainer in regional_team.trainers.all():
                subject = "You've been invited to a horse show"
                email_template = get_template('horseshow/invite.txt')
                d = Context({'username':trainer.username, 'horseshow':new_horse_show,'showteam':new_show_team,'root_url':settings.ROOT_URL})
                message = email_template.render(d)
                send_mail(subject,message,"invitation@tuftshorses.herokuapp.com",[trainer.email])
        new_horse_show.save()
        return new_horse_show

class HorseShow(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.CharField(max_length=400)
    title = models.CharField(max_length=100)
    judge = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    admin = models.ManyToManyField(User)
    hosting_team = models.ForeignKey('Team',null=True)
    classes = models.ManyToManyField('Class')
    teams = models.ManyToManyField('ShowTeam')
    maxriders = models.IntegerField(default=15)
    region = models.ForeignKey('Region', null=True)
    barn = models.CharField(max_length=100)

    objects = HorseShowManager()

class Zone(models.Model):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, null=True)

class Region(models.Model):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, null=True)
    zone = models.ForeignKey(Zone, null=True)

class Team(models.Model):
    school = models.CharField(max_length=100)
    nickname = models.CharField(max_length=5)
    region = models.ForeignKey(Region, null=True)
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
    
class Rider(models.Model):
    user = models.ForeignKey(User)
    showteam = models.ForeignKey('ShowTeam')
    horse = models.ForeignKey(Horse,null=True)
    place = models.IntegerField(default=-1)
    pointed = models.BooleanField(default=True)
    class_type = models.CharField(choices=CLASS_TYPES,max_length=20)

    def points(self):
      if self.place == 1:
        return 7
      elif self.place > 6:
        return 0
      else:
        return 7 - self.place

class ShowTeam(models.Model):
    team = models.ForeignKey(Team)
    riders = models.ManyToManyField(User,through=Rider,related_name='show_team_riders')
    trainers = models.ManyToManyField(User,related_name='show_team_trainers')

    def points(self):
      p = 0
      for r in Rider.objects.filter(showteam=self):
        p += r.points()
      return p

INVITATION_STATUSES = (
    (-1, "Unanswered"),
    (1, "Attending"),
    (0, "Not Attending"),
)

class ShowInvitationManager(models.Manager):
    def create(self,*args,**kwargs):
        try:
            invite = self.get(rider=kwargs['rider'],showteam=kwargs['showteam'])
        except self.model.DoesNotExist:
            invite = super(ShowInvitationManager,self).create(*args,**kwargs)
            rider = kwargs['rider']
            showteam = kwargs['showteam']
            show = showteam.horseshow_set.get()
            subject = "Your coach wants you to participate in a show"
            email_template = get_template('horseshow/requestrider.txt')
            d = Context({'username':rider.username, 'horseshow':show,'showteam':showteam,'root_url':settings.ROOT_URL,'uuid':invite.uuid})
            message = email_template.render(d)
            send_mail(subject,message,"invitation@tuftshorses.herokuapp.com",[rider.email])
        return invite

class ShowInvitation(models.Model):
    showteam = models.ForeignKey(ShowTeam)
    rider = models.ForeignKey(User)
    status = models.IntegerField(choices=INVITATION_STATUSES,default=-1)
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)

    objects = ShowInvitationManager()

class Class(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(choices=CLASS_TYPES, max_length=20)
    division = models.CharField(choices=DIVISION_TYPES,max_length=20)
    order = models.IntegerField(default=-1)
    eventLength = models.IntegerField(default=10)
    horses = models.ManyToManyField(Horse,through='Membership')
    riders = models.ManyToManyField(Rider)
  
class Membership(models.Model):
    horse = models.ForeignKey(Horse)
    event_class = models.ForeignKey(Class)
    alternate = models.BooleanField(default=False)
    able = models.BooleanField(default=True) 
    height_limit = models.IntegerField(default=300) #inches
    weight_limit = models.IntegerField(default=300) #pounds

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


