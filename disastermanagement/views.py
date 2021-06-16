from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'disastermanagement/index.html')

def about(request):
    return render(request,'disastermanagement/about.html')

def floods(request):
    return render(request,'disastermanagement/floods.html')

def droughts(request):
    return render(request,'disastermanagement/droughts.html')

def cyclones(request):
    return render(request,'disastermanagement/cyclones.html')

def earthquakes(request):
    return render(request,'disastermanagement/earthquakes.html')

def landslides(request):
    return render(request,'disastermanagement/landslides.html')

def pandemic(request):
    return render(request,'disastermanagement/pandemic.html')

def donate(request):
    if request.method == 'POST':
        donor=Donors()
        donor.first_name=request.POST.get('first_name')
        donor.last_name=request.POST.get('last_name')
        donor.phone=request.POST.get('phone')
        donor.email=request.POST.get('email')
        donor.amount=request.POST.get('amount')
        donor.save()
        return render(request,'disastermanagement/donate1.html',{
            "amount":donor.amount
        })
    return render(request, 'disastermanagement/donate.html')

@csrf_exempt
def success(request):
    return render(request, "disastermanagement/success.html")

def volunteer(request):
    return render(request,'disastermanagement/volunteer.html')

def help(request):
    return render(request,'disastermanagement/help.html')

def contact(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        description=request.POST.get('description')

        send_mail(
            'message from  ' + first_name + " " + last_name + '  -  ' + message, #subject
            '\n' + description + '\n\n' + 'Sincerely,\n\n' + first_name + ' ' + last_name+'\n'+ email+'\n'+ phone, #message
            email, #from email
            ['patil.neha08@yahoo.com'],#to email
        )
        return render(request,'disastermanagement/contact.html',{
            "message":"Message successfully sent."
        })
    return render(request,'disastermanagement/contact.html')
