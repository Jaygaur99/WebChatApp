import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .helpers import two_username_to_one_username

import json
from django.contrib.auth import get_user_model

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def home(request):
    user = get_user_model()
    all_users = user.objects.all()
    return render(request,'chat_room/home.html', {'allusers' : all_users })

# def chat_person(request):
#     User = get_user_model()
#     email = request.POST.get('email')
#     name = request.POST.get('name')
#     user = User.objects.get(email=email)
#     usernames = two_username_to_one_username(email, request.user.email)
#     print(usernames)
#     return render(request, 'chat_room/chat.html', {'user':user, 'name':name, 'usernames':usernames})

def chat_person(request):
    User = get_user_model()
    email = request.user.email
    # print(json.loads(request.body))
    name = json.loads(request.body).get('id')
    # print(name)
    user = User.objects.get(id=name)
    usernames = two_username_to_one_username(email, user.email)
    # print(usernames)
    return render(request, 'chat_room/chat.html', {'user':user, 'name':name, 'usernames':usernames})

def index(request):
    return render(request, 'chat_room/index.html')

def searchhandle(request):
    User = get_user_model()
    if request.method == 'POST':
        email_or_name = request.POST['email']
        user_list = User.objects.filter(email__icontains=email_or_name)
        print(user_list)
        return render(request,'chat_room/results.html', context={'user_list': user_list})
    else:
        return redirect('chat_room/home.html')

def autocompletion(request):
    User = get_user_model()
    user = request.GET.get('email')
    emails = []
    # print(user)
    if user:
        user_objs = User.objects.filter(email__contains = user)
        for obj in user_objs:
            emails.append((obj.email))
        # print(emails)
    return JsonResponse({'status':200,'data':emails},safe=False)