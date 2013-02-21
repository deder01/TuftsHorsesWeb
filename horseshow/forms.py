from django.contrib.auth.models import *
from horseshow.models import *
from django import forms

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fences_division','flat_division')
    def __init__(self, *args, **kwargs):
        super(DivisionForm,self).__init__(*args,**kwargs)
        self.fields['fences_division'].widget.attrs['class'] = 'span1'
        self.fields['flat_division'].widget.attrs['class'] = 'span1'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

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