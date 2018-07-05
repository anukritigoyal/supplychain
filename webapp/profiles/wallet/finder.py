import os
from .wal_client import WalClient
import requests
import hashlib
import json
import base64
from base64 import b64encode

WAL_NAMESPACE = hashlib.sha512('wal'.encode("utf-8")).hexdigest()[0:6]

def _get_keyfile(usrname):
	username = usrname
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

def query(name,usrname,url):
	#url has to be changed
	# url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile(usrname)
	client = WalClient(base_url=url,keyfile = keyfile)
	print(name)

	response = client.show(name=name)
	return response

def query_all(url):
	url = url + '/state'

	r = requests.get(url = url)
	allstates = r.json()
	
	jsan = {}
	j=0
	for i in allstates['data']:
		if i['address'][0:6]== WAL_NAMESPACE:
			jsan[j] = (base64.b64decode(i['data']))
			j = j+1
	return jsan

