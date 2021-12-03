import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .helpers import two_username_to_one_username
from django.template.loader import render_to_string

import json
from django.contrib.auth import get_user_model
from  django.urls import reverse
from django.http import JsonResponse, request
from django.shortcuts import render, HttpResponse, redirect

from .models import Message
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

    m = Message.objects.all()
    lst = []
    for message in m:
        if message.content != "":
            lst.append(("text", message.content.replace(":","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")))
            continue
        lst.append(("file", message.file.url))
        file = lst
    # print("/n/nFILE/n/n",file)
    messages = []
    i = -1
    for obj in Message.objects.filter(chat_identifier=usernames):
        i += 1
        messages.append({ 
            'message': lst[i][1],
            'from_user': obj.from_user,
            'to_user': obj.to_user,
            'type' : lst[i][0]
        })

    print(messages)
    return render(request, 'chat_room/chat.html', {
        'user':user,
        'name':name,
        'usernames':usernames,
        'messages': messages,
        'file' : file,
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
         new_file = Message(
             file = request.FILES['doc']
         )
         new_file.save(force_insert=True)
         files = []
         files.append(new_file)
         return render(request,'chat_room/chat2.html',{'uploaded_file': new_file})
    #      render(request, 'chat_room/chat.html', {
    #       'user':user,
    #       'name':name,
    #       'usernames': usernames,
    #       'messages': messages,
    #       'uploaded_file': new_file
    #       })
    #      return render(request,'chat_room/home.html', {'allusers' : all_users })
    #  else:
    #      return render(request,'chat_room/upload.html')

# lst = []
#     ...: for message in m:
#     ...:     if message.content != "":
#     ...:         lst.append({"type" : "text","msg":message.content})
#     ...:         continue
#     ...:     lst.append({"type":"file","path":message.file})

def temp(request):
    m = Message.objects.all()
    lst = []
    for message in m:
        if message.content != "":
            lst.append(("text", message.content))
            continue
        lst.append(("file", message.file.path))
    file = lst[-3]
    messages = []
    for obj in Message.objects.filter(chat_identifier=usernames):
        messages.append({ 
            'message': obj.content.split(":")[1],
            'from_user': obj.from_user,
            'to_user': obj.to_user
        })
    print(messages)
    return render(request,'chat_room/temp.html', {'file': file})