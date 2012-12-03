from tastypie.resources import ModelResource
from horseshow.models import *
from tastypie.authorization import Authorization
from tastypie import fields

class HorseResource(ModelResource):
    class Meta:
        queryset = Horse.objects.all()
        resource_name = 'horse'
        authorization = Authorization()

class HorseShowResource(ModelResource):
	hostingBarn = fields.ForeignKey('BarnResource','hostingBarn')
	horseShowDays = fields.ToManyField('HorseShowDayResource','horseshowdays',full=True)
	class Meta:
		queryset = HorseShow.objects.all()
		resource_name = 'horseshow'

class BarnResource(ModelResource):
	class Meta:
		queryset = Barn.objects.all()
		resource_name = 'barn'

class HorseShowDayResource(ModelResource):
    class Meta:
        queryset = HorseShowDay.objects.all()
        resource_name = 'horseshowday'
        authorization = Authorization()

class RingResource(ModelResource):
	class Meta:
		queryset = Ring.objects.all()
		resource_name = 'ring'

class TrainerResource(ModelResource):
	class Meta:
		queryset = Trainer.objects.all()
		resource_name = 'trainer'

class RiderResource(ModelResource):
	class Meta:
		queryset = Rider.objects.all()
		resource_name = 'rider'

class DivisionResource(ModelResource):
	class Meta:
		queryset = Division.objects.all()
		resource_name = 'division'