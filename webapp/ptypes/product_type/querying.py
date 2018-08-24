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