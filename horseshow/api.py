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
	admin = fields.ToManyField(UserResource,'admin',full=True)
	hostingBarn = fields.ForeignKey('horseshow.api.BarnResource','hostingBarn',full=True)
	horseShowDays = fields.ToManyField('horseshow.api.HorseShowDayResource','horseShowDays',full=True)
	class Meta:
		queryset = HorseShow.objects.all()
		resource_name = 'horseshow'
        
class BarnResource(ModelResource):
    owner = fields.ForeignKey(UserResource,'owner',full=True)
    riders = fields.ToManyField(UserResource,'riders',full=True)
    trainers = fields.ToManyField(UserResource,'trainers',full=True)
    class Meta:
        queryset = Barn.objects.all()
        resource_name = 'barn'

class HorseShowDayResource(ModelResource):
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

class TrainerResource(ModelResource):
	details = fields.ForeignKey(UserResource,'details',full=True)
	barn = fields.ForeignKey(BarnResource,'barn',full=True)
	riders = fields.ToManyField('horseshow.api.RiderResource','riders',full=True)
	class Meta:
		queryset = Trainer.objects.all()
		resource_name = 'trainer'

class RiderResource(ModelResource):
    details = fields.ForeignKey(UserResource,'details',full=True)
    horse = fields.ForeignKey('horseshow.api.HorseResource','horse',full=True)
    class Meta:
        queryset = Rider.objects.all()
        resource_name = 'rider'

class DivisionResource(ModelResource):
    riders = fields.ToManyField('horseshow.api.RiderResource','riders',full=True)
    class Meta:
        queryset = Division.objects.all()
        resource_name = 'division'
