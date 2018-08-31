# Forms that are created with the help of models.py. These forms are used in views.py and rendered in the corresponding HTML pages

from django.contrib.auth.models import User
from django import forms
from .models import ItemCreation
from .models import ItemSending

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']


#Create a form for creation of item
#Code reuse :D

#probably will hit me 
class CreateItemForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ItemCreation
		fields = ['itemname','password','ptype']

class SendItemForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ItemSending
		fields = ['recv','password']