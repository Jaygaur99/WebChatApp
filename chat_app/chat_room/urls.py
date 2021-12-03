from os import name
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'chat_room'

urlpatterns = [    
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('chat_person/', chat_person, name='chat_person'),
    path('searchhandle/',searchhandle,name='searchhandle'),
    path('search/',autocompletion,name='autocompletion'),
    path('fileshare/',fileshare,name='fileshare'),
    path('upload/',upload,name='upload'),
    path('temp/',temp,name="temp")

]