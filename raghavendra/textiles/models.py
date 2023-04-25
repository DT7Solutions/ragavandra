from datetime import datetime
from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.

class RegisterUsers(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=20, blank=False)
    LastName = models.CharField(max_length=20, blank=False)
    EmailID = models.EmailField()
    Phone = models.IntegerField(max_length=10,)
    Password = models.CharField(max_length=25, blank=False)
    Address =  models.CharField(max_length=255,null=True, blank=True)
    City =  models.CharField(max_length=25,null=True, blank=True)
    State =  models.CharField(max_length=25,null=True, blank=True)
    Zip = models.CharField(max_length=10,default=0,null=True, blank=True)
    UserStatus = models.BooleanField(default=True)

    def __int__(self):
            return self.UserID
    
class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Name  = models.CharField(max_length=30,null=True, blank=True)
    WhatsappNo = models.IntegerField(max_length=10,null=True, blank=True)
    ContactNo = models.IntegerField(max_length=10,null=True, blank=True)
    Address = models.CharField(max_length=250, blank=False)
    street_name = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=255,null=True, blank=True)
    state = models.CharField(max_length=255,null=True, blank=True)
    postal_code = models.CharField(max_length=10,null=True, blank=True)
    Courier = models.CharField(max_length=30, blank=False)
    TrackingId = models.CharField(max_length=10,default=0,null=True, blank=True)
    No_Of_Items = models.IntegerField(max_length=10,null=True, blank=True)
    file = models.FileField(upload_to='media/')
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    OrderStatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    Date = models.DateTimeField(default=datetime.now())
    UserID = models.ForeignKey('RegisterUsers', on_delete=models.CASCADE) 
   
    def __int__(self):
            return self.OrderID
    