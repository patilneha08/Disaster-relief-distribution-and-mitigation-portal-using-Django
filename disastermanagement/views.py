from django.shortcuts import render, redirect 
from django.http import HttpResponse

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
    return render(request,'disastermanagement/donate.html')

def volunteer(request):
    return render(request,'disastermanagement/volunteer.html')

def help(request):
    return render(request,'disastermanagement/help.html')

def contact(request):
    return render(request,'disastermanagement/contact.html')