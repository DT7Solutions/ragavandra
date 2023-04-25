from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.

class RegisterUsers(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, blank=False)
    LastName = models.CharField(max_length=20, blank=False)
    EmailID = models.EmailField()
    Phone = models.CharField(max_length=10, unique=True)
    Password = models.CharField(max_length=25, blank=False)
    Address =  models.CharField(max_length=255,null=True, blank=True)
    City =  models.CharField(max_length=25,null=True, blank=True)
    State =  models.CharField(max_length=25,null=True, blank=True)
    Zip = models.CharField(max_length=10,default=0,null=True, blank=True)
    UserStatus = models.BooleanField(default=True)
  
    def __int__(self):
            return self.UserID
    