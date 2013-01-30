# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *

def home(request):
  return render_to_response('index.hamlpy', context_instance=RequestContext(request, {}))

def barn(request, barnid):
  barn = Barn.objects.all().filter(id=barnid)[0]
  barnname = barn.title
  return render_to_response('teams/'+barnname.lower()+'/index.hamlpy',
                            context_instance=RequestContext(request, {
                              'barnname':barnname,
                              }))
