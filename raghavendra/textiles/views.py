from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import RegisterUsers
# Create your views here.
def home(request):
    return render(request ,"uifiles/home.html")

def createAccount(request):
    if request.method=='POST':
        
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        Phone = request.POST.get('Phone',"")
        password = request.POST.get('password',"")

        oUser_info = RegisterUsers(FirstName=fname,LastName=lname,EmailID=email,Phone=Phone,Password=password)
        oUser_info.save()
        return HttpResponseRedirect('/login/')
    
    return render(request ,"uifiles/create-account.html")