# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *

def home(request):
  return render_to_response('index.hamlpy', context_instance=RequestContext(request, {}))

def team(request, teamid):
  team = Team.objects.all().filter(id=teamid)[0]
  teamname = team.title
  return render_to_response('teams/'+teamname.lower()+'/index.hamlpy',
                            context_instance=RequestContext(request, {
                              'teamname':teamname,
                              }))

def show(request, showid):
  show = HorseShow.objects.all().filter(id=showid)[0]
  return render_to_response('shows/'+(show.title).lower()+'/index.hamlpy',
                            context_instance=RequestContext(request, {
                              'show':show,
                              }))
