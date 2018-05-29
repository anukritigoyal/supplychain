import os
from hw_client import HwClient

def _get_keyfile():
	username = 'ubuntu'
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

def check1(name):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)

	response = client.check(name=name,check_no='check1')

	print("response: {}".format(response))

def check2(name):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)

	response = client.check(name=name,check_no='check2')

	print("response: {}".format(response))

def check3(name):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)

	response = client.check(name=name,check_no='check3')

	print("response: {}".format(response))

def check4(name):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)

	response = client.check(name=name,check_no='check4')

	print("response: {}".format(response))