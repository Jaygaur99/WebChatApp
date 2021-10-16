from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome,name='welcome'), # Temporary
    path('login/', login, name='login'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('signup/', signup, name='signup'),
    path('signhandle/', signhandle, name = 'signhandle'),
    path('loginauth/', loginauth, name = 'loginauth')
=======
    path('', home, name='home')
>>>>>>> 9d8e99d6c4b553827d74154271812fbdc5feb2b5
=======
    path('signup/', signup, name='signup'),
    path('signhandle/', signhandle, name = 'signhandle'),
    path('loginauth/', loginauth, name = 'loginauth')
>>>>>>> b2b383746068e94a492b92ba658c0bf0c8c36f7b
]