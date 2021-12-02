import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .helpers import two_username_to_one_username
from django.template.loader import render_to_string

import json
from django.contrib.auth import get_user_model

from django.http import JsonResponse, request
from django.shortcuts import render, HttpResponse, redirect

from .models import Message, Files
# Create your views here.

def home(request):
    global all_users
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
    global User
    global email
    global name
    global user
    global usernames
    global messages
    User = get_user_model()
    email = request.user.email
    name = json.loads(request.body).get('id')
    user = User.objects.get(id=name)
    usernames = two_username_to_one_username(email, user.email)
    messages = []
    for obj in Message.objects.filter(chat_identifier=usernames):
        messages.append({ 
            'message': obj.content.split(":")[1],
            'from_user': obj.from_user,
            'to_user': obj.to_user
        })
    # print(messages)
    return render(request, 'chat_room/chat.html', {
        'user':user,
        'name':name,
        'usernames':usernames,
        'messages': messages
        })

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

def fileshare(request):
    return render(request, 'chat_room/upload.html')

def upload(request):
    if request.method == 'POST' and 'doc' in request.FILES:
        new_file = Files(
            file = request.FILES['doc']
        )
        new_file.save()
        files = []
        files.append(new_file)
        # return render(request,'chat_room/chat.html',{'uploaded_file': new_file})
        render(request, 'chat_room/chat.html', {
         'user':user,
         'name':name,
         'usernames': usernames,
         'messages': messages,
         'uploaded_file': new_file
         })
        return render(request,'chat_room/home.html', {'allusers' : all_users })
    else:
        return render(request,'chat_room/upload.html')