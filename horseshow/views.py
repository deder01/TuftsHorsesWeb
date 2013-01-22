# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout

def Home(request):
  return render_to_response('index.html', context_instance=RequestContext(request, {}))
