import os 
from .ptype_client import PtypeClient

def _get_keyfile(usrname):
	username = usrname
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")
	return '{}/{}.priv'.format(key_dir, username)

def create_check(name, dept, role, check, adminname, url):
    keyfile = _get_keyfile(adminname)
    ptype_client = PtypeClient(base_url = url, keyfile = keyfile)
    response = ptype_client.create_check(name = name, dept = dept, role = role, check = check)
    return response