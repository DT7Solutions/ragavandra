from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import home,createAccount,Updatepassword,editprofile,orders,logout
urlpatterns = [
    path('',home,name="login"),
    path('forgotpassword/',Updatepassword, name='forgotpassword'),
    path('orders/',orders, name='orders'),
    path('register/',createAccount, name='register'),
    path('profile/',editprofile,name="profile"),
    path('logout/',logout,name="logout"),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)