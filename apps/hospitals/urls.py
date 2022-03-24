from django.urls import path
from . import views

urlpatterns = [

    path('addPatient/', views.addPatient, name="addPatient"),
    path('storePatient/', views.storePatient, name="storePatient"),
    path('', views.dashboard, name="dashboard"),
    path('dashboard/<int:pk>', views.dashboard, name="dashboard"),
    path('updatePatient/<int:pk>', views.updatePatient, name="updatePatient"),
    path('saveupdate/<int:pk>', views.saveupdate, name="saveupdate"),
    path('delete/<int:pk>', views.deletePatient, name="deletePatient"),
    path('doctors/', views.doctors, name="doctors"),
    path('search/', views.search, name="search"),
    path('prescription/<int:pk>', views.prescription, name="prescription"),
    path('storeprescription/', views.storeprescription, name="storeprescription"),
    # path('viewprescription/<int:pk>', views.viewprescription, name="viewprescription"),


]