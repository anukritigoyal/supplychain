from django.db import models

# Create your models here.
class ProfileCreation(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #profile = models.CharField(max_length=30)

class Pair(object):
	def __init__(self,name,pubkey,prof):
		self.name = name
		self.pubkey = pubkey
		self.prof = prof
