from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import RegisterUsers,Orders
# Create your views here.
def home(request):
    if request.method=='POST':
        phone = request.POST.get('phone',"")
        password = request.POST.get('pass',"")
        queryset = RegisterUsers.objects.all()
        for fields in queryset:
            if fields.Phone == int(phone) and fields.Password == password:
                orders = Orders.objects.filter(UserID=fields.UserID)
                userdata = RegisterUsers.objects.filter(UserID=fields.UserID)
                return render(request, 'uifiles/orders.html', {'orders': orders ,'userdata':userdata})
        
    return render(request ,"uifiles/home.html")

def createAccount(request):
    if request.method=='POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('Phone',"")
        password = request.POST.get('password',"")
        person_exists = RegisterUsers.objects.filter(Phone=phone).exists()
        if person_exists:
            return HttpResponseRedirect('/register/')
        else:
           oUser_info = RegisterUsers(FirstName=fname,LastName=lname,EmailID=email,Phone=phone,Password=password)
           oUser_info.save()
           return HttpResponseRedirect('/')
       
    return render(request ,"uifiles/create-account.html")