from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Orders
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.
def home(request):
    if request.method=='POST':
        username = request.POST.get('username',"")
        password = request.POST.get('pass',"")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user )
            return HttpResponseRedirect('/orders/') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request ,"uifiles/home.html")

def createAccount(request):
    if request.method=='POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/register/')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/register/') 
        oUser_info = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
        oUser_info.save()
        return HttpResponseRedirect('/') 
            
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
        Transactionid  = request.POST.get('TransactionNo',"")
        No_of_items = request.POST.get('No_of_items',"")
        up_file = request.FILES['image_file']
        upload_file = settings.MEDIA_URL[1:] + "//img//" + str(up_file.name)
        user_item = Orders.objects.filter(user=request.user)
        oOrder_info = Orders(Name=name,WhatsappNo=whatsapp_No,ContactNo=contact_no,Address=address, street_name=streetname,city=city,state=state,postal_code=postalcode,Courier=courier,TransactionId=Transactionid,No_Of_Items=No_of_items, file=up_file,user=request.user)
        oOrder_info.save()
        message = f'welcome {request.user} thank for order raghavendra textiles '
        send_whatsapp_message(message=message,whatsapp_no=whatsapp_No)
        return HttpResponseRedirect('/orders/')
    orders_list = Orders.objects.filter(user=request.user)
    return render(request ,"uifiles/orders.html" ,{"orders_list":orders_list})


def Updatepassword(request):
    if request.method=='POST':
        username = request.POST.get('Username',"")
        password = request.POST.get('password',"")
        re_password = request.POST.get('re-password',"")
        user_item = User.objects.filter(username = username)
        for user in user_item:
            if user is None:
                messages.error(request, 'user not found')
            elif password != re_password:
                messages.error(request, 'password does not match')
            else:
                hashed_password = make_password(password, hasher='pbkdf2_sha256')
                user.password=hashed_password
                user.save()
                return redirect('/') 
        
    return render(request ,"uifiles/forgotpassword.html")

def editprofile(request):
    return render(request ,"uifiles/profile.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

# @login_required
def send_whatsapp_message(whatsapp_no,message):
    whatsapp_no = "+91"+ str(whatsapp_no)
    message = message
    headers = {"Authorization": settings.WHATSUP_TOKEN}
    payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": whatsapp_no,
            "type": "text",
            "text": {"body": message}
        }
    response = requests.post(settings.WHATSUP_URL, headers=headers, json=payload)
    ans = response.json()
    return  "success"
    
 

# def Sendwhatsappmessage ( whatsapp_No,message):
#     headers={"Authorization":settings.WHATSUP_TOKEN}
#     payload={"messaging_product":"whatsapp",
#              "recipient_type": "individual",
#              "to":whatsapp_No,
#              "type":"text",
#              "text":{"body":message}
#              }
#     response = requests.post(settings.WHATS_URL,headers=headers,json=payload)
#     ans = response.json()
@csrf_exempt
def whatswebhook(request):
    if request.method == 'GET':
        VERFIY_TOKEN = "8f08d35c-d4a3-4ce0-bec8-db786e9a100f"
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERFIY_TOKEN:
            return HttpResponseRedirect(challenge, status =200)
        else:
            return HttpResponseRedirect('error',status=403)
    

    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponseRedirect ('success' ,status=200)