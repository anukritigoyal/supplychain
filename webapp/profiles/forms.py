from django import forms
#from .models import ProfileCreation

from django.contrib.auth.models import User
from .models import ProfileCreation

class CreateProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ProfileCreation
		fields = ['username','password','department']
