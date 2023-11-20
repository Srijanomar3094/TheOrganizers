from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee_details(models.Model):
    employee = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=200)

