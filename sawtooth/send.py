import os
from hw_client import HwClient

def _get_keyfile():
	username = 'ubuntu'
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

def snd(name,nxt_add):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)

	response = client.send(name=name,nxt_add=nxt_add)

	print("response: {}".format(response))

