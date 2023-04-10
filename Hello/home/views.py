from django.shortcuts import render,redirect,HttpResponse
from home.models import Report,Shop
from datetime import datetime
from django.contrib import messages
from .models import icepops
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
    ices = icepops.objects.all()
    return render(request,"index.html", {'ices':ices})
    
def home(request):
    return render(request,"index.html")
    #return HttpResponse("this is jay's home homepage")

def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is jay's about homepage")

def search(request):
    query = request.GET['query']
    all = icepops.objects.filter(name__icontains=query)
    params = {'all':all}
    return render(request,"search.html",params)
    # return HttpResponse("this is jay's search homepage")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.success(request, 'Invalid credentials')
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def shop(request):
    return render(request,"shop.html")

def flavours(request):
    return render(request,"flavours.html")

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email is already taken')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.success(request, 'Registration done')
                return redirect("login")
        else:
            messages.success(request, 'Password and confirm password is not matching')
    return render(request,"register.html")

    


def report(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        report = Report(name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        report.save()
        messages.success(request, 'Your message has been sent')
    return render(request,"report.html")

def shop(request):
    if request.method == "POST":
        desc = request.POST.get('desc')
        paymentMethod = request.POST.get('paymentMethod')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        shop = Shop(paymentMethod=paymentMethod,name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        shop.save()
        messages.success(request, 'Your delicious dessert will be delivered soon')
    return render(request,"shop.html")
    