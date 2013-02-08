from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from models import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.conf import settings
from forms import *

def send_invite(request):
    if request.method ==  'POST':
        invite_form = InvitationForm(request.user,data=request.POST)
        if invite_form.is_valid():
            invite = invite_form.save()
            clearance = invite.clearance
            profile = request.user.profile
            if clearance == 'rider':
                
            return HttpResponseRedirect("/")
    else:
        invite_form = InvitationForm(request.user)
    return render_to_response('invitations/send_invite.hamlpy',
                              {'form':invite_form},
                              context_instance=RequestContext(request))

def register(request,invite_uuid):
    if request.user.is_authenticated():
        logout(request)
    invite = get_object_or_404(Invite,uuid=invite_uuid)
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            clearance = invite.clearance
            if clearance == 'rider':
                new_user.is_rider = True
            if clearance == 'trainer':
                new_user.is_trainer = True
            if clearance == 'zone director':
                new_user.is_zone_director = True
            if clearance == 'regional director':
                new_user.is_region_director = True
            new_user.save()
            return HttpResponseRedirect("/register/success/")
    else:
        register_form = RegistrationForm()
    return render_to_response('invitations/register.hamlpy',
                              {'form':register_form},
                              context_instance=RequestContext(request))

def confirm_registration(request,uuid):
    registration = get_object_or_404(Registration,uuid=uuid)
    Registration.objects.activate_user(uuid)
    return render_to_response('invitations/register_confirm.hamlpy',
                              context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('invitations/register_success.hamlpy',
                              context_instance=RequestContext(request))