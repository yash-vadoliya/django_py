from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.user.is_anonymous():
        return render(request, 'login.html')
    return render(request, 'index.html')

    # return HttpResponse('This is Homepage')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is Aboutpage')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if username is not None:
            return render(request, 'login.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'login.html')
        

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        contact = Contact(name=name, email=email, mobile=mobile, date=datetime.today())
        contact.save()
        messages.success(request, "Submit Data Successfully...")
    return render(request, 'contact.html')
