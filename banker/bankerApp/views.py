from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from tkinter import messagebox
from bankerApp.forms import MyForm


# Create your views here.
def bankIndex(request):
    return render(request,'index.html')

def Register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['password']
        cpassw = request.POST['cpassword']
        if passw == cpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username is already taken")
                return redirect('/Register')
            else:
                user = User.objects.create_user(username=uname, password=passw,)
                user.save()
                print("user created")
        else:
            # print("password mismatching")
            messages.info(request, "password mismatch")
            return redirect('/Register')
        return redirect('/login')
    return render(request,'register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/login')
    return render(request,'login.html')

def Home(request):
    return render(request,'home.html')
def requirments(request):
    form = MyForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            def load_cities(request):
                country_id = request.GET.get('country')
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
    return render(request,'requirments.html',{'form': form})
# views.py
from django.http import JsonResponse
from .models import City

def get_cities(request, country_id):
    cities = City.objects.filter(country_id=country_id)
    city_options = '<option value="">---------</option>'
    for city in cities:
        city_options += f'<option value="{city.pk}">{city.name}</option>'
    return JsonResponse(city_options, safe=False)
def logout(request):
    auth.logout(request)
    return redirect('/')
def successmsg(request):
    if request.method == 'POST':
        messagebox.showinfo('title',"successful submission")
    return render(request,'index.html')
