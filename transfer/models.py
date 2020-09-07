from django.db import models

# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    mail=models.EmailField(max_length=254)
    feed=models.CharField(max_length=254)
    country=models.CharField(max_length=25)
