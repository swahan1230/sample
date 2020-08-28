from django.db import models

# Create your models here.
class User(models.Model):
    usr_image=models.ImageField(upload_to='media/')
