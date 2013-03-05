from django.contrib.auth.models import *
from horseshow.models import *
from django import forms
from widgets import BootstrapSplitDateTimeWidget as DateTimeWidget, CheckboxMultipleSelect
from django.forms.widgets import SplitDateTimeWidget, CheckboxSelectMultiple

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

class ShowForm(forms.ModelForm):
    def __init__(self,team,*args,**kwargs):
        super(ShowForm,self).__init__(*args,**kwargs)
        self.fields['date'] = forms.SplitDateTimeField(input_date_formats=["%m/%d/%Y"],input_time_formats=["%I:%M\
            %p"],error_messages={'invalid_time':'Enter a valid time (7:00 AM, 12:00 PM, 7:00 PM)',
                                 'invalid_date': 'Enter a vlid date (03/02/2013)'
                                 })

        self.fields['date'].widget = SplitDateTimeWidget(date_format="%m/%d/%Y",time_format="%I:%M %p",attrs={'class':'datepicker-default'})
        self.team = team

    def save(self):
        self.cleaned_data['hosting_team'] = self.team
        horseshow = HorseShow.objects.create(**self.cleaned_data)
        horseshow.region = self.team.region
        horseshow.save()
        return horseshow
    class Meta:
        model = HorseShow
        fields = ('title','date','barn','location','lat','lng','maxriders')

class RosterForm(forms.Form):
    fences_riders = forms.ModelMultipleChoiceField(widget=CheckboxMultipleSelect,queryset=User.objects.none())
    flat_riders = forms.ModelMultipleChoiceField(widget=CheckboxMultipleSelect,queryset=User.objects.none())

    def __init__(self,showteam,*args,**kwargs):
        super(RosterForm,self).__init__(*args,**kwargs)
        self.showteam = showteam
        self.fields['fences_riders'].queryset = showteam.team.riders.all()
        self.fields['flat_riders'].queryset = showteam.team.riders.all()

    def save(self):
        self.showteam.rider_set.all().delete()
        for user in self.cleaned_data['fences_riders']:
            Rider.objects.create(user=user,showteam=self.showteam,class_type="fences").save()
            ShowInvitation.objects.create(rider=user,showteam=self.showteam)
        for user in self.cleaned_data['flat_riders']:
            Rider.objects.create(user=user,showteam=self.showteam,class_type="flat").save()
            ShowInvitation.objects.create(rider=user,showteam=self.showteam)
        return self.showteam

class AttendanceForm(forms.ModelForm):
    def save(self):
        invite = super(AttendanceForm,self).save()
        invite.save()
        if invite.status == 0:
            Rider.objects.filter(showteam=invite.showteam,user=invite.rider).delete()
            # TODO: Notify trainers that a chosen rider cannot compete
        return invite

    class Meta:
        model = ShowInvitation
        fields = ('status',)
        
        
class ClassForm(forms.ModelForm):
    def __init__(self,show,*args,**kwargs):
        super(ClassForm,self).__init__(*args,**kwargs)
 
    def save(self,show):
        klass = Class.objects.create(**self.cleaned_data)
        klass.horseshow_set.add(show)
        klass.save()
        return klass
    class Meta:
        model = Class
        fields = ('title','type','division','eventLength')
