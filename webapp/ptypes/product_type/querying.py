import os
from .ptype_client import PtypeClient
import hashlib
import base64
from base64 import b64encode
import requests
import json

PTYPE_NAMESPACE = hashlib.sha512('ptype'.encode("utf-8")).hexdigest()[0:6]

def query_all(url):
    url = url + '/state'

    request = requests.get(url = url)
    states = request.json()
    
    all_details = {}
    j = 0
    for i in states['data']:
        if i['address'][0:6] == PTYPE_NAMESPACE:
            all_details[j] = (base64.b64decode(i['data']))
            j = j + 1
    
    return all_details

def query_one(name, username, url):
    keyfile = get_keyfile(username)
    client = PtypeClient(base_url = url, keyfile = keyfile)
    response = client.show(name = name)
    response = deserialize(response)



def get_keyfile(username):
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

class Ptype(object):
    def __init__(self, ptype_name, dept, role):
        self.name = ptype_name
        self.dept = dept
        self.role = role

def deserialize(data):
		ptypes = {}
		try:
			for ptype in data.decode().split("|"):
				name,dept,role = ptype.split(",")
				ptypes[name] = Ptype(name,dept,role)

		except ValueError:
			pass
			
		return ptypes