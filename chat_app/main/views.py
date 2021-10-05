from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def home(request):
    e_id = request.POST['Email_ID']
    password = request.POST['Password']
    data = {
        'email_id' : e_id,
        'password' : password,
    }
    if request.method == 'POST' and e_id and password:
        return render(request,'home.html',data)
    else:
        return render(request,'login.html')