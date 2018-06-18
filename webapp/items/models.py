from django.db import models

# Create your models here.

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
        self.long = longi
        if iheld == None:
            self.iheld = 1
        else:
            self.iheld = iheld
        


