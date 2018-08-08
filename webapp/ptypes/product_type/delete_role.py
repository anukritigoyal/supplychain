import os 
from .ptype_client import PtypeClient

def _get_keyfile(adminname):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.priv'.format(key_dir, adminname)

def delete_role(name, dept, role, adminname, url):
    keyfile = _get_keyfile(adminname)
    ptype_client = PtypeClient(base_url = url, keyfile = keyfile)
    response = ptype_client.delete_role(name = name, dept = dept, role = role)
    return response