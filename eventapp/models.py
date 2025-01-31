from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to='img')
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    
class User(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField
    password=models.CharField(max_length=100)