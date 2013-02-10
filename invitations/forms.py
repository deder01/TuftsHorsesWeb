from django.contrib.auth.models import *
from invitations.models import *
from django import forms
from horseshow.models import Profile
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(),
                               label=u'username')
    email = forms.EmailField(label=u'email address')
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=u'password')
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=u'password (again)')

    def clean_username(self):
        alnum_re = re.compile(r'^\w+$')
        if not alnum_re.search(self.cleaned_data['username']):
            raise forms.ValidationError(_(u'Usernames can only contain letters, numbers and underscores'))
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u'This username is already taken. Please choose another.')

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(u'You must type the same password each time')
        return self.cleaned_data
    
    def save(self):
        new_user = Registration.objects.create_inactive_user(username=self.cleaned_data['username'],
                                                                    password=self.cleaned_data['password1'],
                                                                    email=self.cleaned_data['email'])
        return new_user

class InvitationForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(InvitationForm, self).__init__(*args,**kwargs)
        choices = []
        if user.is_staff or user.is_superuser:
            choices = CLEARANCES
        else:
            userprofile = user.profile
            if userprofile.is_rider and user.captainTeam.count()>0:
                choices = CLEARANCES[:1]
            if userprofile.is_trainer:
                choices = CLEARANCES[:2]
            if userprofile.is_region_director:
                choices = CLEARANCES[1:2]
            if userprofile.is_zone_director:
                choices = CLEARANCES[2:3]
        self.fields['clearance'] = forms.ChoiceField(choices=choices)

    def save(self):
        new_invite = Invite.objects.create_invite(self.cleaned_data['email_address'],
                                                  self.cleaned_data['clearance'])
        return new_invite

    class Meta:
        model = Invite
        fields = ('email_address','clearance')