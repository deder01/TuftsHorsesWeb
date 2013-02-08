from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from models import *
from django.http import HttpResponseRedirect
from django.conf import settings
from forms import *

def send_invite(request):
    if request.method ==  'POST':
        invite_form = InvitationForm(request.user,data=request.POST)
        if invite_form.is_valid():
            invite = invite_form.save()
            return HttpResponseRedirect("/")
    else:
        invite_form = InvitationForm(request.user)
    return render_to_response('invitations/send_invite.hamlpy',
                              {'form':invite_form},
                              context_instance=RequestContext(request))

def register(request,invite_uuid):
    invite = get_object_or_404(Invite,uuid=invite_uuid)
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            return HttpResponseRedirect("/register/sucess/")
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