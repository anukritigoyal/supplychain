from django.shortcuts import render,redirect
from .sawtooth import querying
from django.http import Http404
from django.contrib.auth import authenticate, login
from .sawtooth import finder as finder_saw
from .sawtooth import his
from .sawtooth import checks
import json
import time
from profiles.wallet import finder as finder_wal
from .forms import UserForm
from django.views import View
# Create your views here.


def index(request):
	#response = querying.query_all_items()
	response = querying.query_user_held(request.user.username)
	
	resp = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		nc_add = finder_wal.query(c_add,request.user.username)
		nc_add = _deserialize_key(nc_add)

		'''np_add = finder.query(prev_add,'ubuntu')
								np_add = _deserialize_key(np_add)
								'''
		resp[name] = Item(name,checks,nc_add,prev_add)


	
	context = {'resp' :resp}

	return render(request,'items/index.html', context)

def detail(request,itemname):
	#find item uses state list 
	response = finder_saw.find(itemname,'ubuntu')
	
	resp = _deserialize(response)
	nc_add = finder_wal.query(resp[itemname].c_addr,'ubuntu')
	nc_add = _deserialize_key(nc_add)
	resp[itemname].c_addr = nc_add
	#get the checks list
	checks_list = checks.item_checks_list(resp[itemname].check)
	#hist goes through transactions in BC, so returns in human readble form
	hist= his.item_history(itemname)
	print(resp[itemname].check)
	print(resp[itemname].name)



	context = {'resp' :resp,'hist' : hist , "checks_list" : checks_list}
	return render(request,'items/detail.html',context)	

def checked(request,itemname):
	checks.check(itemname,'ubuntu',request.POST['check'],'ubuntu')
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





def create(request):
	return None

def map(request):
	return render(request,'items/map.html')




#LOGIN Stuff

class UserFormView(View):
	form_class = UserForm
	template_name = 'items/login_form.html'
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)
		print("Posting atleast")

		username = request.POST['username']
		password  =request.POST['password']
		user = authenticate(username=username,password=password)
		print("User authenticate")
		if user is not None:
			
			login(request,user)
			return redirect('items:index')

		return render(request,self.template_name,{'form':form})
			


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
			raise InternalError("Failed to deserialize items data")

		return items

def _deserialize_key(data):
	
		for pair in data.decode().split("|"):
			name,pubkey,prof = pair.split(",")
			
		return name 
		