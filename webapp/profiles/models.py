from django.db import models

# Create your models here.
class ProfileCreation(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

class Pair(object):
	def __init__(self,name,pubkey,prof):
		self.name = name
		self.pubkey = pubkey
		self.prof = prof

class history_object(object):
    def __init__(self,name,action,c_addr,p_addr,timestamp):
        self.name = name
        self.action = action
        self.c_addr = c_addr
        self.p_addr = p_addr
        self.timestamp = timestamp
