from django.urls import path
from .views import home,createAccount
urlpatterns = [
    path('',home,name="login"),
    path('register/',createAccount, name='register'),

    
]