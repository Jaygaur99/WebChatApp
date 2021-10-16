from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'), # Temporary
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('signhandle/', signhandle, name = 'signhandle'),
    path('loginauth/', loginauth, name = 'loginauth'),
    path('change_password/', change_password, name = 'change_password'),
    path('otp/', otp, name='otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('new_password', new_password, name='new_password'),
]