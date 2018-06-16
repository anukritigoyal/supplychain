from django.contrib.auth.models import User
from django import forms
from .models import ItemCreation

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','password']


#Create a form for creation of item
#Code reuse :D

#probably will hit me 
class CreateItemForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ItemCreation
		fields = ['item','password']