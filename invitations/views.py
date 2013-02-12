from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from models import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.conf import settings
from horseshow.models import *
from forms import *

def forgot_password(request):
    if request.method == 'POST':
        username_form = RequestPasswordResetForm(data=request.POST)
        if username_form.is_valid():
            username_form.save()
            return render_to_response('invitations/forgot_password_success.hamlpy',
                                      context_instance=RequestContext(request))
    else:
        username_form = RequestPasswordResetForm()
    return render_to_response('invitations/forgot_password_form.hamlpy',
                               context_instance=RequestContext(request,{
                                'form':username_form,
                                }))

def reset_password(request,reset_uuid):
    password_reset = get_object_or_404(PasswordReset,uuid=reset_uuid)
    if request.method == "POST":
        reset_form = ResetPasswordForm(password_reset.user,data=request.POST)
        if reset_form.is_valid():
            reset_form.save()
            return render_to_response('invitations/reset_password_success.hamlpy',
                                      context_instance=RequestContext(request))
    else:
        reset_form = ResetPasswordForm(password_reset.user)
    return render_to_response('invitations/reset_password_form.hamlpy',
                               context_instance=RequestContext(request,{
                                'form':reset_form,
                                }))

def send_invite(request):
    if request.method ==  'POST':
        invite_form = InvitationForm(request.user,data=request.POST)
        if invite_form.is_valid():
            invite = invite_form.save()
            clearance = invite.clearance
            profile = request.user.profile
            if clearance == 'rider':
                if profile.is_rider:
                    invite.context = request.user.riderTeam.all()[0]
                elif profile.is_trainer:
                    invite.context = request.user.trainerTeam.all()[0]
            if clearance == 'trainer':
                if profile.is_trainer:
                    invite.context = request.user.trainerTeam.all()[0]
                if profile.is_region_director:
                    if not profile.is_trainer:
                        new_team = Team.objects.create(school="",nickname="",region=request.user.region_set.all()[0],
                                                       lat=0,lng=0,location="")
                        new_team.save()
                        invite.context = new_team
                        invite.creates_context = True
            if clearance == 'regional director':
                if profile.is_region_director:
                    invite.context = request.user.zone_set.all()[0]
                elif profile.is_zone_director:
                    new_region = Region.objects.create(title="",zone=request.user.zone_set.all()[0])
                    new_region.save()
                    invite.context = new_region
                    invite.creates_context = True
            if clearance == 'zone director':
                new_zone = Zone.objects.create(title="")
                new_zone.save()
                invite.context = new_zone
                invite.creates_context = True
            invite.save()
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
                new_user.profile.is_rider = True
                if invite.context is not None:
                    team = invite.context
                    team.riders.add(new_user)
                    team.save()
            if clearance == 'trainer':
                new_user.profile.is_trainer = True
                if invite.context is not None:
                    team = invite.context
                    team.trainers.add(new_user)
                    team.save()
            if clearance == 'zone director':
                new_user.profile.is_zone_director = True
                if invite.context is not None:
                    zone = invite.context
                    zone.admin = new_user
                    zone.save()
            if clearance == 'regional director':
                new_user.profile.is_region_director = True
                if invite.context is not None:
                    region = invite.context
                    region.admin = new_user
                    region.save()
            new_user.save()
            new_user.profile.save()
            invite.created_user = new_user
            invite.save()
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