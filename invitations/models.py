from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1

CLEARANCES = (
    ('rider','Rider'),
    ('trainer','Trainer'),
    ('regional director','Regional Director'),
    ('zone director','Zone Director')
)

class Invite(models.Model):
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)
    clearance = models.CharField(max_length=40,default='rider')
    date_issued = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    email_address = models.CharField(max_length=400,default="")
    created_user = models.ForeignKey(User,null=True)

class Registration(models.Model):
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)
    user = models.ForeignKey(User)
    date_issued = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
