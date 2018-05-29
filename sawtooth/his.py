import os
from hw_client import HwClient
import requests
import hashlib
import json
import base64
from base64 import b64encode

'''
def _get_keyfile():
	username = 'ubuntu'
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)
'''

HW_NAMESPACE = hashlib.sha512('hw'.encode("utf-8")).hexdigest()[0:6]


def make_item_address(name):
	return HW_NAMESPACE + \
		hashlib.sha512(name.encode('utf-8')).hexdigest()[:64]



def history(name):
	url = 'http://127.0.0.1:8008/transactions'
	#keyfile = _get_keyfile()
	r = requests.get(url=url)
	alltrans = r.json()
	address = make_item_address(name)

	for i in alltrans['data']:
		if i['header']['outputs'] == [address]:
			print(base64.b64decode(i['payload']))


	#print(alltrans['data'][1]['payload'])


