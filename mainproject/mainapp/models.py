from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.
class Client(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=10)

class Registration(forms.Form):
	first_name = forms.CharField(label='Enter First Name', min_length=4, max_length=50)
	last_name = forms.CharField(label='Enter Last Name', min_length=4, max_length=50)
	contact_number = forms.CharField(label='Enter Contact no.', max_length=10)


class Registrationform(forms.ModelForm):
	class Meta:
		model = Client
		fields=['first_name','last_name','contact_number']