# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# from app.accounts.models import Profile 

class customer_customerinfo(models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	mobile = models.CharField(max_length=15,validators=[phone_regex], blank=True)
	city = models.CharField(max_length=15, blank=True)
	invite_code = models.CharField(max_length=15, blank=True)

	def __unicode__(self):
		return self.driver_name

class user_customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	customer = models.OneToOneField(customer_customerinfo, on_delete=models.CASCADE)

# @receiver(post_save, sender=customer_customerinfo)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#     	print instance
#         user = User.objects.create(username=instance,email=instance.email, password=instance.password)
#         save_relation(instance, user)
#         create_customer_profile(user)
# def create_customer_profile(instance):
# 	Profile.objects.create(user=instance, user_type='CA')
# 	save_customer_profile(instance)
# def save_customer_profile(instance):
# 	instance.profile.save()

# def save_relation(customer, userid):
# 	user_customer.objects.create(user=userid, customer=customer)