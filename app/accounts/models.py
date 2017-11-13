# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	user_type_choices = (
	    ('MV', 'Mover'),
	    ('CA', 'Customer'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=100,choices=user_type_choices)
	bio = models.TextField(max_length=500, blank=True)
	location =models.CharField(null=True,max_length=300)
	birth_date = models.DateField(null=True,blank=True)

	def __unicode__(self):
		return "%s" %(self.user_type)