from tastypie.resources import ModelResource
from horseshow.models import *
from tastypie.authorization import Authorization
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']

class HorseResource(ModelResource):
    class Meta:
        queryset = Horse.objects.all()
        resource_name = 'horse'
        authorization = Authorization()

class HorseShowResource(ModelResource):
    hostingBarn = fields.ForeignKey('BarnResource','hostingBarn')
    horseShowDays = fields.ToManyField('HorseShowDayResource','horseShowDays',full=True)
    class Meta:
        queryset = HorseShow.objects.all()
        resource_name = 'horseshow'
        
class BarnResource(ModelResource):
    owner = fields.ForeignKey('UserResource','owner')
    riders = fields.ToManyField('UserResource','riders',full=True)
    trainers = fields.ToManyField('UserResource','trainers',full=True)
    class Meta:
        queryset = Barn.objects.all()
        resource_name = 'barn'

class HorseShowDayResource(ModelResource):
    rings = fields.ToManyField('RingResource','rings',full=True)
    trainers = fields.ToManyField('TrainerResource','trainers',full=True)
    class Meta:
        queryset = HorseShowDay.objects.all()
        resource_name = 'horseshowday'
        authorization = Authorization()

class RingResource(ModelResource):
    divisions = fields.ToManyField('DivisionResource','divisions',full=True)
    class Meta:
        queryset = Ring.objects.all()
        resource_name = 'ring'

class TrainerResource(ModelResource):
    barn = fields.ForeignKey(BarnResource,'barn')
    riders = fields.ToManyField('RiderResource','riders',full=True)
    class Meta:
        queryset = Trainer.objects.all()
        resource_name = 'trainer'

class RiderResource(ModelResource):
    horse = fields.ForeignKey('HorseResource','horse')
    class Meta:
        queryset = Rider.objects.all()
        resource_name = 'rider'

class DivisionResource(ModelResource):
    riders = fields.ToManyField('RiderResource','riders',full=True)
    class Meta:
        queryset = Division.objects.all()
        resource_name = 'division'
