from django.shortcuts import render
from .sawtooth import querying
from django.http import Http404
from .sawtooth import finder
import json

# Create your views here.

def index(request):
	response = querying.query_all_items()
	print(response)
	resp = {}
	for s in response:
		name,checks,c_add,prev_add = response[s].decode().split(",")
		resp[name] = Item(name,checks,c_add,prev_add)
	print(resp)
	context = {'resp' :resp}

	return render(request,'items/index.html', context)

def detail(request,itemname):

	response = finder.find(itemname,'ubuntu')
	items = _deserialize(response)

	
	return render(request,'items/detail.html',items)	

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