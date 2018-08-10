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

class CreatePageView(View):
    product_form = ProductTypeForm
    template_name = 'ptypes/create.html'

    def get(self, request):
        if request.user.is_authenticated == False:
            return redirect('items:login')

        form = self.product_form(None)
        return render(request, self.template_name, {'form' : form})
