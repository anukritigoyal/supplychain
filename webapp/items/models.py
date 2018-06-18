from django.db import models

# Create your models here.

class ItemCreation(models.Model):
    itemname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class ItemSending(models.Model):
    recv = models.CharField(max_length = 30)
    password = models.CharField(max_length=30)