from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *

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

def pandemic(request):
    return render(request,'disastermanagement/pandemic.html')

def donate(request):
    if request.method=='POST':
        donation=Donors()
        donation.first_name=request.POST.get('first_name')
        donation.last_name=request.POST.get('last_name')
        donation.email=request.POST.get('email')
        donation.phone=request.POST.get('phone')
        donation.amount=request.POST.get('amount')
        return render(request,'disastermanagement/payment.html',{
            "donation":donation
        })
        
    return render(request,'disastermanagement/donate.html')

def volunteer(request):
    return render(request,'disastermanagement/volunteer.html')

def help(request):
    return render(request,'disastermanagement/help.html')

def contact(request):
    return render(request,'disastermanagement/contact.html')

def payment(request):
    pass