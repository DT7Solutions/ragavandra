from django.contrib import admin
from .models import RegisterUsers, Orders

class AdminRegister(admin.ModelAdmin):
    list_display=('UserID','FirstName','LastName','EmailID','Phone','Password')

class AdminOrder(admin.ModelAdmin):
    list_display=('OrderID','Name','WhatsappNo','ContactNo','Address','OrderStatus','file','TransactionId')
    list_filter= ['Name','WhatsappNo','TransactionId']
# Register your models here.
admin.site.register(RegisterUsers,AdminRegister)
admin.site.register(Orders,AdminOrder)


