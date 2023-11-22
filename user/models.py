from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
   
    

