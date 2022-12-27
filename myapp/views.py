from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .form import appointmentForm
# Create your views here.
def home(request):
    all_doc = Doctor.objects.all()

    return render(request, 'home.html', {'all_doc':all_doc})

def registerview(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.info(request,'username already found try with another')
            return redirect('register')

        if User.objects.filter(email = email).exists():
            messages.info(request,'invalid email id')
            return redirect('register')


        usr = User(username = username,email = email)
        usr.set_password(password)
        usr.save()


    return render(request, 'register.html')

def loginviews(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():

            aa = authenticate(username = username,password= password)
            if aa:
                login(request,aa)
                return redirect('home')

            else:
                messages.info(request,'invalid password')
                return redirect('login')

        else:
            messages.info(request,'incorrect username')
            return redirect('login')

    return render(request,'login.html')



def logoutviews(request):

    logout(request)
    return redirect('home')


def appointment(request):
    if request.method == 'POST':
        name = request.POST['pname']
        age = request.POST['age']
        city = request.POST['city']
        date = request.POST['date']
        time = request.POST['time']
        number = request.POST['number']

        patient = Appointment(name = name,age = age,city = city,date = date,time = time, number =number)
        patient.save()

    allpatient = Appointment.objects.all()

    return render(request,'appointment.html',{'allpatient':allpatient})

def deletedata(request,id):
    dlt = Appointment.objects.get(id=id)
    dlt.delete()
    return redirect('home')

def edit(request,id):
    if request.method == 'POST':
        edt = Appointment.objects.get(id=id)
        form = appointmentForm(request.POST,instance = edt)

        if form.is_valid:
            form.save()
            return redirect('appointment')
    edt = Appointment.objects.get(id=id)
    form = appointmentForm(instance = edt)
    return render(request,'edit.html',{'form':form})