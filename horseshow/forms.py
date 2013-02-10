from django.contrib.auth.models import *
from horseshow.models import *
from django import forms

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ('title',)

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ('title',)

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('school','nickname','lat','lng','location')