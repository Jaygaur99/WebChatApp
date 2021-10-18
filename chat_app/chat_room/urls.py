from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'chat_room'

urlpatterns = [    
    path('', home, name='home'),
]


