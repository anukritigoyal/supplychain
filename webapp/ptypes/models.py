from django.db import models

# Create your models here.
class ProductType(models.Model):
    ptype_name = models.CharField(max_length = 100)
    role_name = models.CharField(max_length = 100)
    check_assign = models.CharField(max_length = 100)