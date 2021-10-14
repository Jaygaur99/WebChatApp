from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 

# Create your views here.
def login(request):
    return render(request,'main/login.html')

def home(request):
    if request.method == 'POST':
        e_id = request.POST['Email_ID']
        password = request.POST['Password']
        data = {
            'email_id' : e_id,
            'password' : password,
        }
        if e_id and password:
            return render(request,'main/home.html',data)
        else:
            return render(request,'main/login.html')
    else:
        return render(request,'main/login.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")