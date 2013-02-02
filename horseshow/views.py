# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *

def user_login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
  return redirect('horseshow.views.home')

def user_logout(request):
  logout(request)
  return redirect('horseshow.views.home')

def home(request):
  if request.user.is_authenticated() == False:
    return render_to_response('login.hamlpy', context_instance=RequestContext(request, {}))
  teamid = str(request.user.riderTeam.all()[0].id)
  return HttpResponseRedirect('/team/'+teamid)

def team(request, teamid):
  team = request.user.riderTeam.all()[0]
  teamname = team.school.lower()
  return render_to_response('teams/'+teamname+'/index.hamlpy',
                            context_instance=RequestContext(request, {
                              'team':team,
                              'teamname':teamname,
                              }))

def show(request, showid):
  team = Team.objects.all().filter(id=teamid)[0]
  show = HorseShow.objects.all().filter(id=showid)[0]
  return render_to_response('shows/'+show.title.lower()+'/index.hamlpy',
                            context_instance=RequestContext(request, {
                              'team':team,
                              'show':show,
                              }))
