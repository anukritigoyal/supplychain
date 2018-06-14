import os
from hw_client import HwClient
import requests
import hashlib
import json
import base64
from base64 import b64encode

#This is just request that is sent to the rest api running

HW_NAMESPACE = hashlib.sha512('hw'.encode("utf-8")).hexdigest()[0:6]


def make_item_address(name):
	return HW_NAMESPACE + \
		hashlib.sha512(name.encode('utf-8')).hexdigest()[:64]



def history(name):
	url = 'http://127.0.0.1:8008/transactions'
	
	r = requests.get(url=url)
	alltrans = r.json()
	address = make_item_address(name)

	for i in alltrans['data']:
		if i['header']['outputs'] == [address]:
			print(base64.b64decode(i['payload']))





