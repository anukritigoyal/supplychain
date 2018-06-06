import os
from wal_client import WalClient
import subprocess

def _get_keyfile():
	username = 'ubuntu'
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

def add(name):
	url = 'http://127.0.0.1:8008'
	res = subprocess.check_output(["sawtooth","keygen",name])
	keyfile = _get_keyfile(name)
	client = WalClient(base_url=url,keyfile = keyfile)

	response = client.create(name=name)

	print("response: {}".format(response))

