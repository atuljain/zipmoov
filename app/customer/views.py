# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from django.views.generic import *
from django.contrib import messages
from .forms import customer_registration_form
from .models import customer_customerinfo, user_customer
from app.accounts.models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.template import loader
# Create your views here.
class Registration(FormView):    # code for template is given below the view's code
    template_name = "index3.html"
    success_url = '/customer/home'
    form_class = customer_registration_form

    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                data_dict = form.cleaned_data
                data = form.cleaned_data["email"]
            if self.validate_email_address(data) is True:
                '''
                If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
                '''
                associated_customer = customer_customerinfo.objects.filter(Q(email=data))
                if associated_customer.exists():
                    result = self.form_valid(form)
                    messages.error(
                        request, 'Customer is already registered kindly login')
                    return result
                else:
                    customer = customer_customerinfo.objects.create(name=data_dict["name"],email=data_dict['email'],mobile=data_dict['mobile'])
                    user = User.objects.create_user(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                    )
                    user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                    if user is not None:
                       if user.is_active:
                            login(request, user)
                    save_relation(customer, user)
                    create_customer_profile(user)
                    result = self.form_valid(form)
                    messages.success(
                        request, 'An email has been sent to {0}. Please check its inbox to continue reseting password.'.format(data))
                    return result
                    # associated_users = User.objects.filter(
                    #     Q(email=data) | Q(username=data))
                    # if associated_users.exists():
                    #     for user in associated_users:
                    #         print "---"
                    #     result = self.form_valid(form)
                    #     messages.success(
                    #         request, 'An email has been sent to {0}. Please check its inbox to continue reseting password.'.format(data))
                    #     return result
                    # else:
                    #     user = User.objects.create(username=data_dict['email'],email=data_dict['email'], password=data_dict['password'])
                    #     save_relation(customer, user)
                    #     create_customer_profile(user)
                    # result = self.form_invalid(form)
                    # messages.error(
                    #     request, 'No user is associated with this email address')
                    # return result
            else:
                '''
                If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
                '''
            #     associated_users = User.objects.filter(username=data)
            #     if associated_users.exists():
            #         for user in associated_users:
            #             print "---"
            #             # self.reset_password(user, request)
            #         result = self.form_valid(form)
            #         messages.success(
            #             request, "Email has been sent to {0}'s email address. Please check its inbox to continue reseting password.".format(data))
            #         return result
            #     result = self.form_invalid(form)
            #     messages.error(
            #         request, 'This username does not exist in the system.')
            #     return result
            # messages.error(request, 'Invalid Input')
        except Exception as e:
            print(e)
        return self.form_invalid(form)

def home(request):
    if request.method == 'GET':
        if not request.user.is_authenticated():
            return HttpResponse("Oopse something went wrong")
        else:
            user_type = Profile.objects.get(user=request.user).user_type
            if user_type == 'CA':
                context = {
                    'user':request.user,
                    'email':request.user
                }
                return HttpResponse(loader.get_template('customer.html').render(context,request))

            else:
                return HttpResponse("Oopse something went wrong")
    else:
        return HttpResponse('404 not found')
def create_customer_profile(user):
    Profile.objects.create(user=user, user_type='CA')
    save_customer_profile(user)
def save_customer_profile(instance):
    instance.profile.save()

def save_relation(customer, userid):
    user_customer.objects.create(user=userid, customer=customer)