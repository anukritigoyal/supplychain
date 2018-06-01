import os
from hw_client import HwClient

def _get_keyfile():
	username = 'ubuntu'
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")
	return '{}/{}.priv'.format(key_dir, username)


def cr(name):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile()
	client = HwClient(base_url=url,keyfile = keyfile)
	response = client.create(name=name)

	print("response: {}".format(response))

