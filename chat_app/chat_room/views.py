from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def home(request):
    user = get_user_model()
    all_users = user.objects.all()
    return render(request,'chat_room/home.html', {'allusers' : all_users })