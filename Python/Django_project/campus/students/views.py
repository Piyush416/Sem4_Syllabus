from django.shortcuts import render,HttpResponse
from datetime import datetime
from students.models import Contact_Data
from students.models import Person
from django.contrib import messages

def Home(request):
    content = {"htitle":"Home Page"}
    return render(request,"home.html", content)

def About(request):
    content = {"atitle":"About Page"}
    return render(request,"about.html",content)


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # Create a object of class define in model 
        c = Contact_Data(username = name, useremail = email, phone = phone, desc = desc, date = datetime.today())
        c.save()
        messages.success(request, "your message has been sent..")
    return render(request,"contact.html")

   


