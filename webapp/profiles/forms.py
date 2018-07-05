from django import forms
from models import ProfileCreation


class CreateProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = ProfileCreation
		fields = ['itemname','password']
