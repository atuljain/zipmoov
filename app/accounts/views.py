# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Profile
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
	if request.method == 'GET':
		template = loader.get_template('index3.html')
        # if request.user.is_authenticated():
        #     user_type =  Profile.objects.get(user=request.user).user_type
        #     if user_type == 'DA':
        #         return HttpResponse(reverse('mover:home'))
        #     elif user_type == 'CA':
        #         return HttpResponse(reverse('customer:home'))
		context = {
			'user':'None'
		}
		return HttpResponse(template.render(context, request))
	if request.method == 'POST':
		# pass
		return HttpResponse("index post")

def login_fn(request):
	if request.method == 'GET':
		template = loader.get_template('login.html')
		context = {
			'user':'None'
		}
		return HttpResponse(template.render(context,request))
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    if user.is_superuser:
                        return HttpResponse("User is admin user")
                    return HttpResponse("usrertype is staff")
                else:
                    user_type =  Profile.objects.get(user=user).user_type
                    if user_type == 'DA':
                        return HttpResponseRedirect(reverse('mover:home'))
                    elif user_type == 'CA':
                        return HttpResponseRedirect(reverse('customer:home'))
                    else:
                        return HttpResponse("There is no usertype , conatct system admin")
                    return HttpResponse("check whether usertype is mover or customer")
            	return HttpResponse("login is ok")
            else:
            	return HttpResponse("failed inside")
        else:
        	return HttpResponse("failed outside")
        return HttpResponse("failed extra outside")

def thanks(request):
    template = loader.get_template('thanks.html')
    context = {
            'user':'None'
        }
    return HttpResponse(template.render(context, request))

def logout_fn(request):
   logout(request)
   response = HttpResponseRedirect('/')
   return response