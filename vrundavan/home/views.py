from django.shortcuts import render
from .models import product, Feedback

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        messege = request.POST.get('messege')
        feedback = Feedback(name=name, email=email, mobile=mobile, messege=messege)
        feedback.save()
    return render(request, 'contact.html')


def products(request):
    products = product.objects.all()
    return render(request, 'product.html', {'products':products})


def about(request):
    return render(request, 'about.html')