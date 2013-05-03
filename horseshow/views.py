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
from invitations.models import *
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from forms import *
from django.forms.models import modelformset_factory
from django.http import Http404


def getTeam(user):
  team = ''
  if user.profile.is_rider:
    team = (user.riderTeam.all()[0])
  elif user.profile.is_trainer:
    team = (user.trainerTeam.all()[0])
  else:
    return null
  return team

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

    if '@' in username:
      username = User.objects.get(email=username).username
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      try:
        invite = Invite.objects.get(created_user=user)
        if invite.creates_context:
          region_type = ContentType.objects.get(model="region")
          zone_type = ContentType.objects.get(model="zone")
          team_type = ContentType.objects.get(model="team")
          content_type = invite.content_type
          context = invite.context
          invite.delete()
          if content_type == region_type:
            return redirect(reverse('horseshow.views.edit_region',args=(context.id,)))
          if content_type == zone_type:
            return redirect(reverse('horseshow.views.edit_zone',args=(context.id,)))
          if content_type == team_type:
            return redirect(reverse('horseshow.views.edit_team', args=(context.id,)))

      except Exception as inst:
        print type(inst)
    else:
      return redirect('horseshow.views.not_user')
  return redirect('horseshow.views.home')

def user_logout(request):
  logout(request)
  return redirect('horseshow.views.home')

def home(request):
    teamid = str(getTeam(request.user).id)
    if teamid:
      return HttpResponseRedirect('/team/'+teamid)
    else:
      return HttpResponseRedierct('/region'/request.user.zone.id)

def region(request, regionid):
  team = getTeam(request.user)
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
  team = get_object_or_404(Team,id=teamid)
  teamname = team.school.lower()
  return render_to_response('team.hamlpy',
                            context_instance=RequestContext(request, {
                              'team':team,
                              'teamname':teamname
                              }))

def show(request, showid):
  show = get_object_or_404(HorseShow, id=showid)
  team = getTeam(request.user)
  showteam = ShowTeam.objects.get(team=team, horseshow=show)
  teams = sorted(show.teams.all(), key=lambda t: t.points())
  classes = show.classes.all().order_by('order')
  return render_to_response('show.hamlpy',
                            context_instance=RequestContext(request, {
                              'show':show,
                              'teams':teams,
                              'classes':classes,
                              'showteam':showteam
                              }))
def zone(request, zoneid):
  team = getTeam(request.user)
  show = HorseShow.objects.all().get(id=showid)
  return render_to_response('show.hamlpy',
                            context_instance=RequestContext(request, {
                              'show':show,
                              }))

def edit_team(request, teamid):
  team = get_object_or_404(Team,id=teamid)
  if not request.user in team.trainers.all() or request.user.is_staff: # check permissions
    raise Http404 # should be 403
  DivisionFormSet = modelformset_factory(Profile,extra=0,form=DivisionForm) # generate formset class based on model and form
  if request.method == "POST": # see if user has submitted a form
    teamform = TeamForm(instance=team,data=request.POST) # generate teamform from team and POST data
    # generate form set from POST data and queryset (riders on team)
    division_form_set = DivisionFormSet(request.POST,queryset=Profile.objects.filter(user__in=team.riders.all()))
    if teamform.is_valid(): # validate team form
      teamform.save() # save team model
      if division_form_set.is_valid(): # validate formset
        division_form_set.save() # update all riders on team
        return redirect(reverse('horseshow.views.team',args=(teamid)))
  else:
    teamform = TeamForm(instance=team) # create new team form from team model
    # create new formset from queryset
    division_form_set = DivisionFormSet(queryset=Profile.objects.filter(user__in=team.riders.all()))
  return render_to_response('edit_team.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':teamform,
                              'division_form_set':division_form_set
                              }))

def edit_region(request, regionid):
  region = get_object_or_404(Region,id=regionid)
  if request.method == "POST":
    regionform = RegionForm(instance=region,data=request.POST)
    if regionform.is_valid():
      regionform.save()
      return redirect(reverse('horseshow.views.region',args=(regionid,)))
  else:
    regionform = RegionForm(instance=region)
  return render_to_response('edit_region.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':regionform,
                              }))

def edit_zone(request, zoneid):
  zone = get_object_or_404(Zone,id=zoneid)
  if request.method == "POST":
    zoneform = ZoneForm(instance=zone,data=request.POST)
    if zoneform.is_valid():
      zoneform.save()
      return redirect(reverse('horseshow.views.zone',args=(zoneid,)))
  else:
    zoneform = ZoneForm(instance=zone)
  return render_to_response('edit_zone.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':zoneform,
                              }))

def edit_user(request):
  user = request.user
  if request.method == "POST":
    userform = UserForm(instance=user,data=request.POST)
    if userform.is_valid():
      userform.save()
      return redirect(reverse('horseshow.views.home'))
  else:
    userform = UserForm(instance=user)
  return render_to_response('edit_user.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':userform,
                            }))

def new_show(request):
  team = getTeam(request.user)
  if request.method == "POST":
    show_form = ShowForm(team,data=request.POST)
    if show_form.is_valid():
      horse_show = show_form.save()
      return redirect(reverse('horseshow.views.show',args=(horse_show.id,)))
  else:
    show_form = ShowForm(team,initial={'date':datetime.now()})
  return render_to_response('new_horse_show.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':show_form,  
                            }))

def edit_show_team(request,showteamid):
  showteam = get_object_or_404(ShowTeam,id=showteamid)
  fences_riders = map(lambda x:x.user,showteam.rider_set.filter(class_type="fences"))
  flat_riders = map(lambda x:x.user,showteam.rider_set.filter(class_type="flat"))
  if request.method == "POST":
    rosterform = RosterForm(showteam,data=request.POST)
    if rosterform.is_valid():
      rosterform.save()
      pass
  else:
    rosterform = RosterForm(showteam,initial={"fences_riders":fences_riders,"flat_riders":flat_riders})
  zipped_fields = zip(showteam.team.riders.all(),*[boundField for boundField in rosterform])
  non_attending_riders = map(lambda x:x.rider,showteam.showinvitation_set.filter(status=0))
  return render_to_response('edit_roster.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':rosterform,
                              'zipped_fields':zipped_fields,
                              'showteam':showteam,
                              'non_attending_riders':non_attending_riders,
                              }))

def edit_attendance(request,uuid):
  invite = get_object_or_404(ShowInvitation,uuid=uuid)
  if request.method == "POST":
    attendance_form = AttendanceForm(instance=invite,data=request.POST)
    if attendance_form.is_valid():
      attendance_form.save()
  else:
    attendance_form = AttendanceForm(instance=invite)
  return render_to_response('edit_attendance.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':attendance_form,
                              }))

def edit_show(request, showid):
  show = get_object_or_404(HorseShow,id=showid)
  if request.method == "POST":
    show_form = ShowForm(team=show.hosting_team,instance=show,data=request.POST)
    if show_form.is_valid():
      show.save()
      return redirect(reverse('horseshow.views.show',args=(show.id,)))
  else:
    show_form = ShowForm(team=show.hosting_team, instance=show)
  return render_to_response('edit_horse_show.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':show_form,  
                            }))

def create_classes(request, showid):
  show = get_object_or_404(HorseShow,id=showid)
  if request.method == "POST":
    class_form= ClassForm(show,data=request.POST)
    if class_form.is_valid():
      klass = class_form.save(show)
      return redirect(reverse('horseshow.views.show',args=(show.id,)))
  else:
    class_form= ClassForm(show)
  return render_to_response('new_class.hamlpy',
                            context_instance=RequestContext(request,{
                              'form':class_form,  
                            }))

