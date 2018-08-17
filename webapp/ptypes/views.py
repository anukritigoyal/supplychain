from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views import View
import json

from .forms import UserForm, User, ProductTypeForm
from .product_type import create_product_type#, delete_product_type, create_role, delete_role, create_check, delete_check

# def index(request):
#     return HttpResponse("Hello, world. You're at the Ptypes index.")

def random_server():
    urls_list = {'1': 'http://127.0.0.1:8008', '2': 'http://rest-api-0:8008'}
    return urls_list['2']

def index(request):
    if request.user.is_authenticated == False:
        return redirect('items:index')

    context = {'username' : request.user.username} 
    return render(request, 'ptypes/index.html', context)

def create(request):
    adminname = request.user.username
    url = random_server()

    if request.method == "POST":
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            ptype_name = form.cleaned_data['ptype_name']
            role_assign = form.cleaned_data['role_name']
            check_assign = form.cleaned_data['check_assign']

            if role_assign is None: 
                create_product_type.create_ptype(ptype_name, "manufacturing", adminname, url)
            # elif role_assign is not None and check_assign is None:
            #     create_role.create_role(ptype_name, dept, role_assign, None, adminname, url)
            # elif role_assign is not None and check_assign is not None:
            #     create_check.create_check(ptype_name, dept, role_assign, check_assign, adminname, url)

            return redirect('ptpyes/create.html')
            

    else:
        form = ProductTypeForm()
        context = {'form' : form}
        return render(request, 'ptypes/create.html', context)