from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome,name='welcome'), # Temporary
    path('login/', login, name='login'),
<<<<<<< HEAD
    path('signup/', signup, name='signup'),
    path('signhandle/', signhandle, name = 'signhandle'),
    path('loginauth/', loginauth, name = 'loginauth')
=======
    path('', home, name='home')
>>>>>>> 9d8e99d6c4b553827d74154271812fbdc5feb2b5
]