import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import customer_customerinfo

class customer_registration_form(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    mobile = forms.CharField(label='Mobile', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    password = forms.CharField(label="Password", max_length=100)
    confirm_password = forms.CharField(label="Confirm Password", max_length=100)
    invite_code = forms.CharField(label="Invite Code", max_length=100)

    def  clean_username(self):
    	try:
    		user = User.objects.get(username__iexact=self.cleaned_data['email'])
    	except User.DoesNotExist:
    		return self.cleaned_data['email']
    	raise forms.ValidationError(_("Email already exist"))
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data