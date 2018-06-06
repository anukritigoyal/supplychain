# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .sawtooth import create
from .sawtooth import delete
#from .sawtooth import checks 
from .sawtooth import finder
from .sawtooth import his

#add serialllization stuff here only


#item_1/
#check if there exists a keyfile --- probably should go into wallet_tf
#handle authentications somewhere!!!!!!!!!
#error handling when keyfile is non existent

class item_create(APIView):
		
	def post(self,request):
		json_req = json.loads(request.body.decode())
		response = create.cr(json_req["names"],json_req["username"])
		return Response("Creation of item initated")

'''rehaul the check function in the main files
class item_check(APIView):
	def post(self,request):
		json_req = json.loads(request.body.decode())
		checks.check1()

'''	

class item_delete(APIView):
	def post(self,request):
		json_req = json.loads(request.body.decode())
		response = delete.delete(json_req["name"],json_req["username"])
		return Response("Item deletion Initiated")

class user_history(APIView):
	#actually returns all the transactions he is involved irrespective of the tf
	def get(self,request):
		json_req = json.loads(request.body.decode())
		response = his.user_history(json_req["username"])
		return Response(response)


class item_finder(APIView):
	def get(self,request):
		json_req = json.loads(request.body.decode())



class item_history(APIView):
	def get(self,request):
		json_req = json.loads(request.body.decode())
		response = his.item_history(json_req["name"])
