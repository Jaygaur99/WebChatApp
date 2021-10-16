from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome,name='welcome'), # Temporary
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('signhandle/', signhandle, name = 'signhandle'),
    path('loginauth/', loginauth, name = 'loginauth'),
]