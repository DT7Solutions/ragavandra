from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Orders
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method=='POST':
        username = request.POST.get('username',"")
        password = request.POST.get('pass',"")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user )
            return HttpResponseRedirect('/orders/')
    return render(request ,"uifiles/home.html")

def createAccount(request):
    if request.method=='POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        oUser_info = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
        oUser_info.save()
        return HttpResponseRedirect('/login/')
       
    return render(request ,"uifiles/create-account.html")

@login_required
def orders(request):
    
    if request.method=='POST':
        name = request.POST.get('Name',"")
        whatsapp_No = request.POST.get('WhatsappNo',"")
        contact_no = request.POST.get('ContactNo',"")
        address = request.POST.get('Address',"")
        streetname = request.POST.get('streetname',"")
        city = request.POST.get('City',"")
        courier = request.POST.get('Courier',"")
        state = request.POST.get('State',"")
        postalcode = request.POST.get('Postalcode',"")
        state = request.POST.get('State',"")
        No_of_items = request.POST.get('No_of_items',"")
        up_file = request.FILES['image_file']
        upload_file = settings.MEDIA_URL[1:] + "//img//" + str(up_file.name)
        user_item = Orders.objects.filter(user=request.user)
        oOrder_info = Orders(Name=name,WhatsappNo=whatsapp_No,ContactNo=contact_no,Address=address, street_name=streetname,city=city,state=state,postal_code=postalcode,Courier=courier,No_Of_Items=No_of_items, file=up_file,user=request.user)
        oOrder_info.save()
        return HttpResponseRedirect('/orders/')
    orders_list = Orders.objects.filter(user=request.user)
    return render(request ,"uifiles/orders.html" ,{"orders_list":orders_list})

def password(request):
     return render(request ,"uifiles/forgotpassword.html")

def editprofile(request):
    return render(request ,"uifiles/profile.html")

def userlogout(request):
    return render(request ,"uifiles/logout.html")
