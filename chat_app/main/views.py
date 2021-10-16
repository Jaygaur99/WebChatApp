from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth, messages 
from django.contrib.auth.models import User 
from .forms import *
from django.contrib.auth import get_user_model

# Create your views here.
def login(request):
    return render(request,'main/login.html')

def loginauth(request):
    if request.method == 'POST':
        e_id = request.POST['Email_ID']
        password = request.POST['Password']

        user = auth.authenticate(email=e_id, password = password)

        if user is None:
            auth.login(request,user)
            return render(request,'main/home.html')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'main/login.html')
    else:
        return render(request,'main/login.html')

def welcome(request):
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
        # jaygaur99@gmail.com -> jaygaur99
        username = fname + lname

        # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('signup')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('signup')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('signup')
        
        # Create the user
        #myuser = User.objects.create_user(fname,lname, email, pass1,pass2,dob)
        myuser = User.objects.create_user(email=email, fname=fname, lname=lname, dob=dob, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " account has been successfully created")
        return redirect('login')
    else:
        # return HttpResponse("404 - Not found")
        return redirect('signup')