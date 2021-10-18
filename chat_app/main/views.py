from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .forms import *

from django.contrib.auth import get_user_model

User = get_user_model()

from django.conf import settings
from django.core.mail import EmailMessage
import random
from .helpers import *

# Create your views here.
def login_page(request):
    return render(request,'main/login.html')

def loginauth(request):
    if request.method == 'POST':
        e_id = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=e_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return redirect('login')

def home(request):
    return render(request,'main/home.html')

def signup(request):
    form = RegisterForm
    para = {
        'form':form
    }
    return render(request, 'main/form.html', context=para)

def signhandle(request):
    if request.method == "POST":
        # Get the post parameters
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        pass2 = request.POST['password_2']
        dob = request.POST['dob']

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('signup')
        myuser = User.objects.create_user(email=email, fname=fname, lname=lname, dob=dob, password=pass1)
        myuser.save()
        messages.success(request, " account has been successfully created")
        return redirect('login')
    else:
        return redirect('home')

def searchhandle(request):
    if request.method == 'POST':
        email = request.POST['email']
        obj = User.objects.all().filter(email=email)
        print(obj)
        return render(request,'main/home.html',context={'email':obj[0]})
    else:
        return redirect('home')

def change_password(request):
    return render(request, 'main/change_password.html')

def otp(request):
    email = request.POST['email']
    otp = generate_otp()
    try:
        user = User.objects.get(email=email)
    except:
        messages.error(request, "User not found")
    user.otp = otp
    user.save()
    subject, message = generate_otp_mail_fields(otp, user.fname)
    send_mail_helper(subject, message, user.email)
    return render(request, 'main/otp.html', {'email': user.email})

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('my_otp')
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if str(user.otp) == otp:
            return render(request, 'main/new_password.html', {'email': email})
        else:
            error_message = 'Wrong Otp! Please Try Again.'
            return render(request, 'main/otp.html', {'email': email, 'error': error_message})
    else:
        return redirect('login')

def new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password == password_2:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return render(request, 'main/password_changed.html')
        else:
            return render(request, 'main/new_password.html', {'email': email})
    else:
        return redirect('login')

def requests(request):
    if request.method == 'POST':
        return render(request,'main/add_friends.html')
    else:
        return redirect('home')