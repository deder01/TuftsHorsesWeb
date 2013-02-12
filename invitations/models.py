from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from horseshow.models import *
from django.contrib.contenttypes import generic

CLEARANCES = (
    ('rider','Rider'),
    ('trainer','Trainer'),
    ('regional director','Regional Director'),
    ('zone director','Zone Director')
)
class PasswordResetManager(models.Manager):
    def create_password_reset(self,username):
        user = User.objects.get(username=username)
        new_password_reset = self.create(user=user)
        subject = "Reset your Tufts Horses password"
        message = settings.ROOT_URL+"/forgotpassword/"+new_password_reset.uuid
        send_mail(subject,message,"passwords@tuftshorses.herokuapp.com",[user.email])
        return new_password_reset

class PasswordReset(models.Model):
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)
    date_issued = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    objects = PasswordResetManager()

class InviteManager(models.Manager):
    def create_invite(self,email,clearance):
        new_invite = self.create(email_address=email,clearance=clearance)
        subject = "You've been invited to join Tufts Horses"
        message = settings.ROOT_URL+"/invitation/"+new_invite.uuid
        send_mail(subject,message,"invitation@tuftshorses.herokuapp.com",[new_invite.email_address])
        return new_invite


class Invite(models.Model):
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)
    clearance = models.CharField(max_length=40,default='rider')
    date_issued = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    email_address = models.CharField(max_length=400,default="")
    created_user = models.ForeignKey(User,null=True)

    content_type = models.ForeignKey(ContentType,null=True)
    object_id = models.PositiveIntegerField(null=True)
    context = generic.GenericForeignKey('content_type','object_id')
    creates_context = models.BooleanField(default=False)

    objects = InviteManager()

class RegistrationManager(models.Manager):
    def create_inactive_user(self,username,password,email):
        new_user = User.objects.create_user(username,email,password)
        new_user.is_active = False
        new_user.save()

        registration = self.create(user=new_user)
        subject = "Confirm your registration with Tufts Horses"
        message = settings.ROOT_URL+"/register/"+registration.uuid
        send_mail(subject,message,"register@tuftshorses.herokuapp.com",[new_user.email])
        return new_user

    def activate_user(self,uuid):
        try:
            registration = self.get(uuid=uuid)
        except self.model.DoesNotExist:
            return False
        if not registration.used:
            user = registration.user
            user.is_active = True
            user.save()
            registration.used = True
            registration.save()
            return user
        return False

class Registration(models.Model):
    uuid = models.CharField(max_length=100,default=lambda:uuid1().hex)
    user = models.ForeignKey(User)
    date_issued = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    objects = RegistrationManager()