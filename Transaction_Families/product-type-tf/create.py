import os
from .ptype_client import PtypeClient

def _get_keyfile(usrname):
	username = usrname
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")
	return '{}/{}.priv'.format(key_dir, username)


def cr(name,usrname,url):
	keyfile = _get_keyfile(usrname)
	client = PtypeClient(base_url=url,keyfile = keyfile)
	response = client.create(name=name,cu_add=usrname)
	return response	