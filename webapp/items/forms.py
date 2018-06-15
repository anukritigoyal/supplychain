from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharsField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']
		