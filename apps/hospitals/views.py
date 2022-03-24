from django.shortcuts import render, redirect
from .models import SavePatient, Prescription
from ..people.models import Services
from django.contrib import messages

# Create your views here.
def addPatient(request):
    services = Services.objects.all()
    patientList = SavePatient.objects.all()
    count = len(patientList)
    return render(request, "addPatient.html" ,{'services':services, 'count': count})

def storePatient(request):
    s = SavePatient()
    s.name = request.POST.get('name')
    s.age = request.POST.get('age')
    s.weight = request.POST.get('weight')
    s.gender = request.POST.get('gender')
    s.mobile = request.POST.get('mobile')
    s.address = request.POST.get('address')

    sid = request.POST.get('services')

    if sid == "empty":
        messages.warning(request, "Department field is empty. Please fill it again")
        return redirect('/hospitals/addPatient')
    else:
        serv = Services.objects.get(id=sid)
        s.services = serv.services
        s.serv = serv
        s.save()

        messages.success(request, "Patient added Successfully")
        return redirect('/hospitals')


def dashboard(request):
    prescription = Prescription.objects.all()
    patientList = SavePatient.objects.all()

    print("Printing Total number of pt")
    count = len(patientList)
    return render(request, "dashboard.html",{'patientList': patientList,
                                             'count': count,
                                             'prescription':prescription})

def updatePatient(request,pk):
    patients = SavePatient.objects.get(id=pk)
    services = Services.objects.all()
    return render(request, 'updatePatient.html', {'s': patients, 'services': services })


def saveupdate(request,pk):
    s = SavePatient.objects.get(id=pk)
    s.name = request.POST.get('name')
    s.age = request.POST.get('age')
    s.weight = request.POST.get('weight')
    s.gender = request.POST.get('gender')
    s.mobile = request.POST.get('mobile')
    s.address = request.POST.get('address')
    try:
        sid = request.POST.get('services')
        serv = Services.objects.get(id=sid)
        s.services = serv.services
    except:
        s.services = request.POST.get('services')
    s.save()
    return redirect('/hospitals')

def deletePatient(request, pk):
    s = SavePatient.objects.get(id=pk)
    s.delete()
    return redirect('/home')

def doctors(request):
    return render(request,'doctors.html')

def search(request):
    searched = request.GET['searched']
    if len(searched)>20:
        patientList = SavePatient.objects.none()
    else:
        patientListname = SavePatient.objects.filter(name__icontains = searched)
        patientListadd = SavePatient.objects.filter(address__icontains=searched)
        patientList = patientListname.union(patientListadd)

    if patientList.count() == 0:
        messages.warning(request,"No search result found. Please search it again")

    return render(request, 'search.html',{'patientList': patientList, 'searched': searched})

def prescription(request,pk):
    patients = SavePatient.objects.get(id=pk)
    services = patients.serv

    print(services)

    return render(request,'prescription.html',{'patients': patients,'services':services})

def storeprescription(request):
    sp = Prescription()
    sp.tablets = request.POST.get('tablets')
    sp.description = request.POST.get('description')
    print("Storing detailss")

    pid = request.POST.get('patients')
    pt = SavePatient.objects.get(id=pid)
    sp.name = pt.name
    sp.pt = pt
    sp.save()

    return redirect('/hospitals')

# def viewprescription(request,pk):
#     prescription = Prescription.objects.get(id=pk)
#     patients = prescription.pt
#     services = patients.serv
#     return render(request, 'viewprescription.html',{'prescription':prescription,
#                                                     'patients': patients,
#                                                     'services':services})