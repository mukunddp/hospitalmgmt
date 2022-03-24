from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Services
from ..hospitals.models import SavePatient

# Create your views here.

def store(request):
    s = Services()
    s.services = request.POST.get('services')
    s.availability = request.POST.get('availability')
    s.specialist = request.POST.get('specialist')
    s.save()
    return redirect('/services')

def home(request):
    count = SavePatient.objects.all()
    serviceList = Services.objects.all()
    serv=len(serviceList)
    return render(request, "home.html",{'count': count,'serv':serv})

def services(request):
    serviceList = Services.objects.all()
    return render(request, "services.html",{'serviceList':serviceList})

def login(request):
    return HttpResponseRedirect("/accounts/login")

def addServices(request):
    return render(request, "addServices.html")

def updateServices(request,pk):
    services = Services.objects.get(id=pk)
    return render(request, 'updateServices.html', {'s':services})

def deleteService(request, pk):
    services = Services.objects.get(id=pk)
    services.delete()
    return redirect('/services')

def update(request,pk):
    s = Services.objects.get(id=pk)
    s.services = request.POST.get('services')
    s.availability = request.POST.get('availability')
    s.specialist = request.POST.get('specialist')
    s.save()
    return redirect('/services')

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration.html"

def about(request):
    return render(request,'about.html')

