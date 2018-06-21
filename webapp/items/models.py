from django.db import models

# Create your models here.
class Item(object):
	def __init__(self,name,check,c_addr,p_addr):
		self.name = name
		self.check = check
		self.c_addr = c_addr
		self.p_addr = p_addr


class ItemCreation(models.Model):
    itemname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class ItemSending(models.Model):
    recv = models.CharField(max_length = 30)
    password = models.CharField(max_length=30)


class userinfo(object):

    def __init__(self,name,lat,longi,iheld=None):

        self.name = name
        self.lat = lat
        self.longi = longi
        if iheld == None:
            self.iheld = 1
        else:
            self.iheld = iheld
        


