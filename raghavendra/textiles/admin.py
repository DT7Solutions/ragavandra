from django.contrib import admin
from .models import RegisterUsers

class AdminRegister(admin.ModelAdmin):
    list_display=('UserID','FirstName','LastName','EmailID','Phone','Password')
    
# Register your models here.
admin.site.register(RegisterUsers,AdminRegister)