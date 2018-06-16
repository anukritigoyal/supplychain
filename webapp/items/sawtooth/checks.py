import os
from .hw_client import HwClient
from .finder import find

def _get_keyfile(usrname):
	username = usrname
	home = os.path.expanduser("~")
	key_dir = os.path.join(home, ".sawtooth", "keys")

	return '{}/{}.priv'.format(key_dir, username)

#different check functions will be called for different checks

def check(name,cu_add,checkno,usrname):
	url = 'http://127.0.0.1:8008'
	keyfile = _get_keyfile(usrname)
	client = HwClient(base_url=url,keyfile = keyfile)
	finding_item = find(name,usrname)
	if finding_item[name].c_addr == client._signer.get_public_key().as_hex():
		response = client.check(name=name,check_no=checkno,cu_add=client._signer.get_public_key().as_hex())
		return 1
	else:
		return 0


def item_checks_list(check_status):
	checks = {}
	checks[1] = "LAL Test"
	checks[2] = "PDP"
	checks[3] = "Batch Release"
	checks[4] = "Final Product Verification"

	check_entire = {}
	j=0
	for i in checks:
		
		check_entire[j] = check_class(checks[i],check_status[j]== '-')
		j = j+1

	
	return check_entire

#django is making me do this !!!!!
class check_class(object):
	def __init__(self,name,check):
		self.name = name
		self.check = check