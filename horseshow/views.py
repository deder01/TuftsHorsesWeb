# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *
from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile
from django.db.models.signals import post_save

def create_profile(sender, **kw):
    def check_for_profile(user):
      try:
        return Profile.objects.get(user=user)
      except Profile.DoesNotExist:
        return None
    user = kw["instance"]
    if kw["created"] or check_for_profile(user) is None:
        up = Profile(user=user)
        up.save()
post_save.connect(create_profile, sender=User)


def not_user(request):
  return render_to_response('login.hamlpy', context_instance=RequestContext(request, {}))
  
def user_login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
    else:
      return redirect('horseshow.views.not_user')
  return redirect('horseshow.views.home')

def user_logout(request):
  logout(request)
  return redirect('horseshow.views.home')

def home(request):
  teamid = str(request.user.riderTeam.all()[0].id)
  if (not teamid):
    teamid = str(request.user.captainTeam.all()[0].id)
  if (not teamid):
    teamid = str(request.user.trainerTeam.all()[0].id)
  return HttpResponseRedirect('/team/'+teamid)

def region(request, regionid):
  team = request.user.riderTeam.all()[0]
  region = Region.objects.all().get(id=regionid)
  shows = region.horseshow_set.all()
  teams = region.team_set.all()
  standings = []
  for t in teams:
    team_points = [t]
    points = 0
    for st in t.showteam_set.all():
      points += st.points()
    team_points.append(points)
    standings.append(team_points)
  return render_to_response('region.hamlpy',
                            context_instance=RequestContext(request, {
                              'standings':standings,
                              'shows':shows,
                              }))

def team(request, teamid):
  team = request.user.riderTeam.all()[0]
  teamname = team.school.lower()
  return render_to_response('team.hamlpy',
                            context_instance=RequestContext(request, {
                              'teamname':teamname,
                              }))

def show(request, showid):
  team = Team.objects.all().get(id=teamid)
  show = HorseShow.objects.all().get(id=showid)
  return render_to_response('show.hamlpy',
                            context_instance=RequestContext(request, {
                              'show':show,
                              }))
def zone(request, zoneid):
  team = Team.objects.all().get(id=teamid)
  show = HorseShow.objects.all().get(id=showid)
  return render_to_response('show.hamlpy',
                            context_instance=RequestContext(request, {
                              'show':show,
                              }))
