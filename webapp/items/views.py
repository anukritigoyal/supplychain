from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth import authenticate, login , logout
from .sawtooth import querying
from .sawtooth import send
from .sawtooth import create as create_saw
from .sawtooth import finder as finder_saw
from .sawtooth import his
from .sawtooth import checks
import time
import requests as req_lib
from profiles.wallet import finder as finder_wal
from .forms import UserForm,SendItemForm
from .forms import CreateItemForm
from django.views import View
from .models import userinfo


###IMPORTANT SEND ALL DESERIALS TO RESPECTIVE MODULES


def index(request):
	
	if request.user.is_authenticated == False :
		return redirect('items:login')

	if not request.GET.get('q'):
		resp= querying.query_user_held(request.user.username)
		#returns from state table all the datas with c_add as username
	else:
		resp = querying.query_possible_items(request.GET.get("q"))
		#takes care of search form
		
	for name,item_obj in resp.items():
		#finding out human name of the public key holder
		nc_add = finder_wal.query(item_obj.c_addr,request.user.username)
		nc_add = _deserialize_key(nc_add)
		resp[name].c_addr = nc_add

	context = {'resp' :resp}

	return render(request,'items/index.html', context)

def detail(request,itemname):
	
	if request.user.is_authenticated == False :
		return redirect('items:login')


	#find item uses state list 
	resp = finder_saw.find(itemname,'ubuntu')
	
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
	requested_user = request.user.username

	context = {'resp' :resp,'hist' : hist , "checks_list" : checks_list , 'requested_user':requested_user}
	return render(request,'items/detail.html',context)	

def user_detail (request,username):

	if request.user.is_authenticated == False :
		return redirect('items:login')
	
	if not request.GET.get('q'):
		resp= querying.query_user_held(username)
		#returns from state table all the datas with c_add as username
	else:
		resp = querying.query_possible_items(request.GET.get("q"))
		#takes care of search form
		
	for name,item_obj in resp.items():
		#finding out human name of the public key holder
		nc_add = finder_wal.query(item_obj.c_addr,request.user.username)
		nc_add = _deserialize_key(nc_add)
		resp[name].c_addr = nc_add


	context = {'resp' :resp}

	return render(request,'items/index.html', context)
	






def checked(request,itemname):


	if request.user.is_authenticated == False :
		return redirect('items:login')
	
	# if not 'check' in request.POST:
	# 	return redirect('items:detail', itemname)
	response_url = checks.check(itemname, request.user.username,request.POST['check'],request.user.username)
	

	#better way to increment time is to increase exponentially with the number of tries
	start_time = time.time()
	while time.time()-start_time<1.5:
		status = req_lib.get(response_url)
		if status['status'] == 'COMMITTED':
			break
		else:
			continue

	
	#necessary because it takes atleast two secs for the state list to get updated
	#should find a more robust way to do this
	#time.sleep(1.5)
	
	resp = finder_saw.find(itemname,'ubuntu')
	
	#add this deserialize to find itself
	nc_add = finder_wal.query(resp[itemname].c_addr,'ubuntu')
	nc_add = _deserialize_key(nc_add)
	resp[itemname].c_addr = nc_add
	#get the checks list
	checks_list = checks.item_checks_list(resp[itemname].check)
	#hist goes through transactions in BC, so returns in human readble form
	hist= his.item_history(itemname)
	requested_user = request.user.username
	context = {'resp' :resp,'hist' : hist , "checks_list" : checks_list,'requested_user':requested_user}
	return render(request,'items/detail.html',context)

class SendItem(View):
	form_class = SendItemForm
	template_name = 'items/send.html'

	def get(self,request,itemname):

		if request.user.is_authenticated == False :
			return redirect('items:login')

		form = self.form_class(None)
		return render(request,self.template_name,{'form' : form,'itemname' : itemname})

	def post(self,request,itemname):

		if request.user.is_authenticated == False :
			return redirect('items:login')

		recv = request.POST['recv']
		username = request.user.username
		password  =request.POST['password']
		user = authenticate(username=username,password=password)

		if user is not None:
			send.snd(itemname,recv,request.user.username) 
			#time.sleep(1.5)
			return redirect('items:index')
		else:
			#retry password
			form = self.form_class(None)
			return render(request,self.template_name,{'form' : form})




def map(request):
	
	if request.user.is_authenticated == False :
		return redirect('items:login')

	#GeoLocations of users Probably change this entire charade to some other file ????
	locations = {'admin':{'lat' : 42.34, 'longi' : -71.55}, 'Mike@manufacturing':{'lat':42.342, 'longi' : -71.52}, 'Susan@sterilization':{'lat':42.339 , 'longi': -71.53}, 'Quinn@quality':{'lat':42.39 , 'longi': -71.54}}
	
	
	
	response = querying.query_all_items()
	resp = {}
	usersdata = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		nc_add = finder_wal.query(c_add,'ubuntu')
		nc_add = _deserialize_key(nc_add)
		resp[name] = Item(name,checks,nc_add,prev_add)
		
		try:
			usersdata[nc_add].iheld += 1
		except:
			usersdata[nc_add] = userinfo(nc_add,float(locations[nc_add]['lat']),float(locations[nc_add]['longi']))
	

	
	context = {'resp' :resp , 'usersdata' : usersdata}
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
			print("Should not come here")
			return redirect('items:login')

		itemname = request.POST['itemname']
		username = request.user.username
		password  =request.POST['password']
		user = authenticate(username=username,password=password)

		if user is not None:
			response = create_saw.cr(itemname,username)
			print(response)
			#time.sleep(1.5)
			return redirect('items:index')
		else:
			#retry password
			form = self.form_class(None)
			return render(request,self.template_name,{'form' : form})
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
def logout_view(request):
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
		