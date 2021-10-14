from django.shortcuts import render

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