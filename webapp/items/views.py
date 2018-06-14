from django.shortcuts import render
from .sawtooth import querying
from django.http import Http404
from .sawtooth import finder
import json
from profiles.wallet import finder

# Create your views here.

def index(request):
	response = querying.query_all_items()
	
	resp = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		nc_add = finder.query(c_add,'ubuntu')
		nc_add = _deserialize_key(nc_add)
		np_add = finder.query(prev_add,'ubuntu')
		np_add = _deserialize_key(np_add)
		resp[name] = Item(name,checks,nc_add,np_add)


	
	context = {'resp' :resp}

	return render(request,'items/index.html', context)

def detail(request,itemname):

	response = finder.find(itemname,'ubuntu')
	print(response)
	resp = _deserialize(response)
	print(resp)
	context = {'resp' :resp}
	return render(request,'items/detail.html',context)	

def create(request):
	return None

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
		