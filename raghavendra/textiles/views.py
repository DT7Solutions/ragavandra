from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import RegisterUsers,Orders
from django.conf import settings
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

def orders(request):
    name = request.POST.get('Name',"")
    whatsapp_No = request.POST.get('WhatsappNo',"")
    email = request.POST.get('Address',"")
    state_Name = request.POST.get('state_Name',"")
    city = request.POST.get('City',"")
    courier = request.POST.get('Courier',"")
    state = request.POST.get('State',"")
    postalcode = request.POST.get('Postalcode',"")
    email = request.POST.get('State',"")
    state_Name = request.POST.get('Postalcode',"")
    up_file = request.FILES['file']
    upload_file = settings.MEDIA_URL[1:] + "//img//" + str(up_file.name)

    oOrder_info = RegisterUsers()
    oOrder_info.save()


def password(request):
     return render(request ,"uifiles/forgotpassword.html")