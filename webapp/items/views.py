from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from .sawtooth import querying
from .sawtooth import send
from .sawtooth import create as create_saw
from .sawtooth import finder as finder_saw
from .sawtooth import his
from .sawtooth import checks
import time
from profiles.wallet import finder as finder_wal
from .forms import UserForm
from .forms import CreateItemForm
from django.views import View

#imported and not used create,send


def index(request):
	
	if request.user.is_authenticated == False :
		return redirect('items:login')


	response = querying.query_user_held(request.user.username)
	#returns from state table all the datas with c_add as username

	resp = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		
		#finding out human name of the public key holder
		nc_add = finder_wal.query(c_add,request.user.username)
		nc_add = _deserialize_key(nc_add)
		resp[name] = Item(name,checks,nc_add,prev_add)

	context = {'resp' :resp}

	return render(request,'items/index.html', context)

def detail(request,itemname):
	
	if request.user.is_authenticated == False == False :
		return redirect('items:login')


	#find item uses state list 
	response = finder_saw.find(itemname,'ubuntu')
	
	resp = _deserialize(response)
	nc_add = finder_wal.query(resp[itemname].c_addr,'ubuntu')
	nc_add = _deserialize_key(nc_add)
	resp[itemname].c_addr = nc_add
	#get the checks list
	checks_list = checks.item_checks_list(resp[itemname].check)
	#hist goes through transactions in block chain, so returns in human readble form
	
	#serialized make that into an item history class with all the attributes so that django 
	#will not complain
	#we can do the serializtion and breaking up stuff in the his.py
	hist= his.item_history(itemname)

	context = {'resp' :resp,'hist' : hist , "checks_list" : checks_list}
	return render(request,'items/detail.html',context)	

def checked(request,itemname):

	if request.user.is_authenticated == False == False :
		return redirect('items:login')


	checks.check(itemname,'ubuntu',request.POST['check'],'ubuntu')
	#necessary because it takes atleast two secs for the state list to get updated
	#should find a more robust way to do this
	time.sleep(2)
	response = finder_saw.find(itemname,'ubuntu')
	
	resp = _deserialize(response)
	nc_add = finder_wal.query(resp[itemname].c_addr,'ubuntu')
	nc_add = _deserialize_key(nc_add)
	resp[itemname].c_addr = nc_add
	#get the checks list
	checks_list = checks.item_checks_list(resp[itemname].check)
	#hist goes through transactions in BC, so returns in human readble form
	hist= his.item_history(itemname)
	
	context = {'resp' :resp,'hist' : hist , "checks_list" : checks_list}
	return render(request,'items/detail.html',context)


def map(request):
	
	if request.user.is_authenticated == False :
		return redirect('items:login')

	response = querying.query_all_items()
	resp = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		nc_add = finder_wal.query(c_add,'ubuntu')
		nc_add = _deserialize_key(nc_add)
		resp[name] = Item(name,checks,nc_add,prev_add)
		
	context = {'resp' :resp}
	return render(request,'items/map.html', context)


class CreateItemView(View):

	form_class = CreateItemForm
	template_name = 'items/create.html'

	def get(self,request):

		if request.user.is_authenticated == False :
			return redirect('items:login')

		form = self.form_class(None)
		return render(request,self.template_name,{'form' : form})

	def post(self,request):
		
		if request.user.is_authenticated == False :
			return redirect('items:login')

		itemname = request.Post['itemname']
		username = request.user.username
		password  =request.POST['password']
		user = authenticate(username=username,password=password)

		if user is not None:
			response = create_saw.cr(itemname,username)
			time.sleep(2)
			return redirect('items:index')

	

#LOGIN Stuff

class UserFormView(View):
	
	form_class = UserForm
	template_name = 'items/login_form.html'
	
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)
		username = request.POST['username']
		password  =request.POST['password']
		user = authenticate(username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('items:index')

		return render(request,self.template_name,{'form': form})
			
#Create a Logout view
def logout(request):
	if request.user.is_authenticated == False :
		return redirect('items:login')

	logout(request)
	return redirect('items:login')


#shift item to models
class Item(object):
	def __init__(self,name,check,c_addr,p_addr):
		self.name = name
		self.check = check
		self.c_addr = c_addr
		self.p_addr = p_addr


def _deserialize(data):
		items = {}
		try:
			for item in data.decode().split("|"):
				name,check,c_addr,p_addr = item.split(",")
				items[name] = Item(name,check,c_addr,p_addr)

		except ValueError:
			pass
			
		return items

def _deserialize_key(data):
	
		for pair in data.decode().split("|"):
			name,pubkey,prof = pair.split(",")
			
		return name 
		