import os
from hw_client import HwClient

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

	response = client.check(name=name,check_no=checkno,cu_add=cu_add)

	print("response: {}".format(response))

def item_checks_list():
	checks = {}
	checks[0] = "Sterilization of the product"
	checks[1] = "LAL Test"
	checks[2] = "PDP"
	checks[3] = "Batch Release"
	checks[3] = "Final Product Verification"
