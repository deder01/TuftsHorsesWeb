from tastypie.resources import ModelResource
from horseshow.models import *
from tastypie.authorization import Authorization
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['id','username', 'first_name', 'last_name', 'last_login']
        authorization = Authorization()

class HorseResource(ModelResource):
    class Meta:
        queryset = Horse.objects.all()
        resource_name = 'horse'
        authorization = Authorization()

class HorseShowResource(ModelResource):
    admin = fields.ToManyField(UserResource,'admin',full=True)
    hosting_team = fields.ForeignKey('horseshow.api.TeamResource','hosting_team',null=True)
    classes = fields.ToManyField('horseshow.api.ClassResource','classes',full=True, null=True)
    teams = fields.ToManyField('horseshow.api.ShowTeamResource','teams',full=True, null=True)
    class Meta:
        queryset = HorseShow.objects.all()
        resource_name = 'horseshow'
        authorization = Authorization()
        
class TeamResource(ModelResource):
    captains = fields.ToManyField(UserResource,'captains')
    riders = fields.ToManyField(UserResource,'riders')
    trainers = fields.ToManyField(UserResource,'trainers')
    class Meta:
        resource_name = 'team'
        queryset = Team.objects.all()
        authorization = Authorization()

"""class HorseShowDayResource(ModelResource):
    rings = fields.ToManyField('horseshow.api.RingResource','rings',full=True)
    trainers = fields.ToManyField('horseshow.api.TrainerResource','trainers',full=True)
    class Meta:
        queryset = HorseShowDay.objects.all()
        resource_name = 'horseshowday'
        authorization = Authorization()

class RingResource(ModelResource):
    divisions = fields.ToManyField('horseshow.api.DivisionResource','divisions',full=True)
    class Meta:
        queryset = Ring.objects.all()
        resource_name = 'ring'
        authorization = Authorization()

class TrainerResource(ModelResource):
    details = fields.ForeignKey(UserResource,'details',full=True)
    barn = fields.ForeignKey(BarnResource,'barn',full=True)
    riders = fields.ToManyField('horseshow.api.RiderResource','riders',full=True)
    class Meta:
        queryset = Trainer.objects.all()
        resource_name = 'trainer'"""

class RiderResource(ModelResource):
    details = fields.ForeignKey(UserResource,'user',full=True)
    horse = fields.ForeignKey('horseshow.api.HorseResource','horse',full=True)
    #divisions = fields.ForeignKey('horseshow.api.DivisionResource','division_set')
    class Meta:
        authorization = Authorization()
        queryset = Rider.objects.all()
        resource_name = 'rider'
        authorization = Authorization()

class MembershipResource(ModelResource):
    details = fields.ForeignKey('horseshow.api.HorseResource','horse')
    class Meta:
        queryset = Membership.objects.all()
        resource_name = 'membership'
        authorization = Authorization()

class ClassResource(ModelResource):
    horses = fields.ToManyField('horseshow.api.MembershipResource','membership_set',full=True)
    riders = fields.ToManyField('horseshow.api.RiderResource','riders',full=True)
    class Meta:
        queryset = Class.objects.all()
        resource_name = 'class'
        authorization = Authorization()

class ShowTeamResource(ModelResource):
    team = fields.ForeignKey('horseshow.api.TeamResource','team',full=True)
    riders = fields.ToManyField('horseshow.api.RiderResource','rider_set')
    trainers = fields.ToManyField(UserResource,'trainers',full=True)
    class Meta:
        queryset = ShowTeam.objects.all()
        resource_name = 'showteam'
        authorization = Authorization()

