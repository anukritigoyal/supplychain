from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views import View
import json

from .forms import UserForm, User, ProductTypeForm
from .product_type import querying 

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
            ptype_name = form.cleaned_data['ptype_name']
            role_assign = form.cleaned_data['role_name']
            check_assign = form.cleaned_data['check_assign']

            submit = "New Product Type Successfully Created"
            context = {'message' : submit}
            return render(request, 'ptypes/create.html', context)
            return redirect('ptpyes/create.html')
            

    else:
        form = ProductTypeForm()
        context = {'form' : form}
        return render(request, 'ptypes/create.html', context)

def details(request, ptype_name):
    if request.user.is_authenticated == False:
        return redirect('items:index')

    # shifted to index
    # url = random_server()
    # response = querying.query_all(url)
    
    # # new
    # details = {}
    # for data in response:
    #     name, dept, role = response[data].decode().split(",")
    #     details[name] = Ptype(name, dept, role)

    # context = {'resp' : details}
    # return render(request, 'ptypes/details.html', context)

    # new ADD HERE to populate
    url = random_server()

    

class Ptype(object):
    def __init__(self, ptype_name, dept, role):
        self.name = ptype_name
        self.dept = dept
        self.role = role