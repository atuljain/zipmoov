from django import forms
from .models import mover_moverinfo

class mover_registration_form(forms.Form):
    email_m = forms.CharField(label='Email', max_length=100)
    name_m = forms.CharField(label='Name', max_length=100)
    mobile_m = forms.CharField(label='Mobile', max_length=100)
    city_m = forms.CharField(label='City', max_length=100)
    licence_m = forms.CharField(label='licence', max_length=100)
    vehicle_number_m = forms.CharField(label='Vehicle', max_length=100)
    address_m = forms.CharField(label='Address', max_length=100)
    password_m = forms.CharField(label="Password", max_length=100)
    confirm_password_m = forms.CharField(label="Confirm Password", max_length=100)

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