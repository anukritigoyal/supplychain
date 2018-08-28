from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views import View
import json

from .forms import UserForm, User, ProductTypeForm
from .product_type import querying, create_product_type, create_role, create_check

def random_server():
	urls_list = { '1': 'http://127.0.0.1:8008','2': 'http://rest-api-0:8008' }
	return urls_list['2']

def index(request):
    if request.user.is_authenticated == False:
        return redirect('items:index')

    url = random_server()
    response = querying.query_all(url)
    
    # new
    details = {}
    for data in response:
        name, dept, role = response[data].decode().split(",")
        details[name] = Ptype(name, dept, role)

    context = {'username' : request.user.username, 'resp' : details} 
    return render(request, 'ptypes/index.html', context)

def create(request):
    if request.method == "POST":
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            username = request.user.username
            dept = username.split("@")
            dept = dept[1]
            url = random_server()

            ptype_name = form.cleaned_data['ptype_name']
            role_assign = form.cleaned_data['role_name']
            check_assign = form.cleaned_data['check_assign']

            # when form allows individual submissions
            if role_assign is None and check_assign is None:
                create_product_type.create_ptype(name = ptype_name, dept = dept, adminname = username, url = url)
            elif role_assign is not None and check_assign is None:
                create_role.create_role(name = ptype_name, dept = dept, role = role_assign, check = None, adminname = username, url = url)
            elif check_assign is not None:
                create_check.create_check(name = ptype_name, dept = dept, role = role_assign, check = check_assign, adminname = username, url = url)


            create_check.create_check(ptype_name, 'manufacturing', role_assign, check_assign, username, url)

            submit = "New Product Type Successfully Created"
            context = {'form': form, 'message' : submit}
            return render(request, 'ptypes/create.html', context)
            

    else:
        form = ProductTypeForm()
        context = {'form' : form}
        return render(request, 'ptypes/create.html', context)

def details(request, ptype_name):
    if request.user.is_authenticated == False:
        return redirect('items:index')

    url = random_server()
    # response is a dictionary with one key value pair - key is ptype name, value is Ptype object
    response = querying.query_one(ptype_name, request.user.username, url)
    
    context = {'response' : response}
    return render(request, 'ptypes/details.html', context)

class Ptype(object):
    def __init__(self, ptype_name, dept, role):
        self.name = ptype_name
        self.dept = dept
        self.role = role