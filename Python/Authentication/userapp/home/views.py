from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , logout , login

def index(request):
    if request.user.is_anonymous:
        return redirect('/login/')
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        id = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=id, password=pwd)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')
