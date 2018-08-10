from django.contrib.auth.models import User
from django import forms
from .models import ProductType

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        #fields = ['username', 'password', 'dept'] 
        fields = ['username', 'password']

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['ptype_name', 'role_assign', 'check_assign']