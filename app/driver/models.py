# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from app.accounts.models import Profile 

class mover_moverinfo(models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	mobile = models.CharField(max_length=15,validators=[phone_regex], blank=True)
	city = models.CharField(max_length=15, blank=True)
	
	def __unicode__(self):
		return self.driver_name

class user_mover(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mover = models.OneToOneField(mover_moverinfo, on_delete=models.CASCADE)

# @receiver(post_save, sender=mover_moverinfo)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         user = User.objects.create(username=instance,email=instance.email, password=instance.password)
#         save_relation(instance, user)
#         create_mover_profile(user)
# def create_mover_profile(instance):
# 	Profile.objects.create(user=instance, user_type='MV')
# 	save_mover_profile(instance)
# def save_mover_profile(instance):
# 	instance.profile.save()

# def save_relation(mover, userid):
# 	user_mover.objects.create(user=userid, mover=mover)