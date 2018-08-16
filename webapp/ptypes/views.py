from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views import View
import json

from .forms import UserForm, User, ProductTypeForm

# def index(request):
#     return HttpResponse("Hello, world. You're at the Ptypes index.")

def index(request):
    if request.user.is_authenticated == False:
        return redirect('items:index')

    context = {'username' : request.user.username} 
    return render(request, 'ptypes/index.html', context)

def create(request):
    if request.method == "POST":
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            ptype_name = form.cleaned_data['ptype_name']
            role_assign = form.cleaned_data['role_name']
            check_assign = form.cleaned_data['check_assign']
            

    else:
        form = ProductTypeForm()
        context = {'form' : form}
        return render(request, 'ptypes/create.html', context)