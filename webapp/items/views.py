from django.shortcuts import render
from .sawtooth import querying
from django.http import Http404
from .sawtooth import finder

# Create your views here.

def index(request):
	response = querying.query_all_items()
	print(response)
	#json to dict
	#response = {1: {name:jo}, 2:{name:sj}}

	return render(request,'items/index.html', dictresp)

def detail(request,itemname):

	try:
		response = finder.find(itemname,'ubuntu')
		dictresp = _deserialize(response)

	except:
		raise Http404("Item Doesn't exist")

	return render(request,'items/detail.html',dictresp)	

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