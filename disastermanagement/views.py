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
        donor=Donor()
        donor.first_name=request.POST.get('first_name')
        donor.last_name=request.POST.get('last_name')
        donor.phone=request.POST.get('phone')
        donor.amount=request.POST.get('amount')
        donor.email=request.POST.get('email')
        donor.save()
        return render(request,'disastermanagement/donate1.html',{
            "amount":donor.amount
        })
    return render(request, 'disastermanagement/donate.html')

@csrf_exempt
def success(request):
    return render(request, "disastermanagement/success.html")

def volunteer(request):
    if request.method=="POST":
        ngos=NGO.objects.all()
        volunteer=Volunteer()
        volunteer.first_name=request.POST.get('first_name')
        volunteer.last_name=request.POST.get('last_name')
        volunteer.email=request.POST.get('email')
        volunteer.phone=request.POST.get('phone')
        volunteer.altphone=request.POST.get('altphone')
        volunteer.gender=request.POST.get('gender')
        volunteer.age=request.POST.get('age')
        volunteer.address=request.POST.get('address')
        volunteer.bloodgroup=request.POST.get('bloodgroup')
        volunteer.aadhar=request.POST.get('aadhar')
        volunteer.service=request.POST.get('service')
        volunteer.save()
        request.session['volunteer']=volunteer.id
        return render(request,'disastermanagement/selectngo.html',{
            "volunteer":volunteer, "ngos":ngos
        })
    return render(request, 'disastermanagement/volunteer.html')


def help(request):
    if request.method=="POST":
        service=request.POST.get('service')
        if service=="Nursing":
            temp=Hospital.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Medicine Supply":
            temp=Chemist.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Emergency Medical Support":
            temp=Hospital.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Medical Equipment Supply":
            temp=Chemist.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Basic Amenities (blankets/clothes/food/water etc.)":
            temp1=NGO.objects.all()
            temp2=General_Store.objects.all()
            temp=temp1+temp2
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Groceries":
            temp=Grocerie.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Basic tools(flashlight/batteries/knife etc.)":
            temp=General_Store.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Vaccines":
            temp=Hospital.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Other":
            temp=NGO.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
        elif service=="Rescue":
            temp=Rescue.objects.all()
            return render(request,'disastermanagement/service.html',{
                "temp":temp
            })
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
            '\n' + description + '\n\n' + 'Sincerely,\n\n' + first_name + ' ' + last_name+'\n'+ email +'\n'+ phone, #message
            email, #from email
            ['patil.neha08@yahoo.com'],#to email
        )
        return render(request,'disastermanagement/contact.html',{
            "message":"Message successfully sent."
        })
    return render(request,'disastermanagement/contact.html')

def selectngo(request, ngo_id):
    if request.method == 'POST':
        temp=ngo_id
        ngo=NGO.objects.get(id=temp)
        volunteer=Volunteer.objects.get(id=request.session["volunteer"])

        send_mail(
            'Volunteer request from  ' + volunteer.first_name + " " + volunteer.last_name, #subject
            '\nThis is to inform you that I, ' + volunteer.first_name + " " + volunteer.last_name  + ', would like to become a volunteer at your esteemed organization. My details are as follows-\n\nName-  ' + volunteer.first_name + " " + volunteer.last_name + "\nContact Number-  +91" + str(volunteer.phone) + "\nAlternate Contact Number-  +91" + str(volunteer.altphone) + "\nEmail Address-  " + volunteer.email + "\nGender-  " + volunteer.gender + "\nAge-  " + str(volunteer.age) + "\nAddress: \n" + volunteer.address + "\nBlood Group-  " + volunteer.bloodgroup + "\nAadhar Number-  "+ str(volunteer.aadhar) + "\nServices provided-  " + volunteer.service + "\n\nKindly look into the matter and do the needful at the earliest." + "\n\nSincerely,\n\n" + volunteer.first_name + ' ' + volunteer.last_name, #message
            settings.EMAIL_HOST_USER, #from email
            [ngo.email],#to email
            fail_silently=False,
        )
        return render(request,'disastermanagement/volunteer.html',{
            "message":"Request successfully sent."
        })
    return render(request,'disastermanagement/selectngo.html')
