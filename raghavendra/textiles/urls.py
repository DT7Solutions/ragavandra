from django.urls import path
from .views import home,createAccount,password
urlpatterns = [
    path('',home,name="login"),
    path('forgotpassword/',password, name='forgotpassword'),
    path('register/',createAccount, name='register'),
   

    
]