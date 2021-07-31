from django.shortcuts import render
from django.http import HttpResponse
from .models import PatientDB
from django.contrib import messages
from django.views import View

# Create your views here.


class index(View):
    def get(self, request):
        return render(request, 'index.html')


class addPatient(View):
    def get(self, request):
        return render(request, 'addPatient.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        age = int(request.POST.get('age'))
        disease = request.POST.get('disease')
        fees = int(request.POST.get('fees'))
        startMedsDate = request.POST.get('startMedsDate')
        doctoreName = request.POST.get('doctor')

        Patient = PatientDB(firstName=fname, lastName=lname, gender=gender, age=age,
                            disease=disease, doctorName=doctoreName, doctorFees=fees, startMedsDate=startMedsDate)
        try:
            Patient.save()
            messages.add_message(request, messages.INFO,
                                 'Patient Added Successfully ')
        except:
            messages.add_message(request, messages.ERROR,
                                 'Somthing gone wrong !! ')

        return render(request, 'addPatient.html')


class patientList(View):
    def get(self, request):
        patients = PatientDB.objects.all()
        return render(request, 'patientList.html', {'patients': patients})


class editPatient(View):
    def get(self, request):
        id = request.GET.get('id')
        patient = PatientDB.objects.get(id=id)
        return render(request, 'edit.html', {'patient': patient})

    def post(self, request):
        patients = PatientDB.objects.all()
        id = request.POST.get('pid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        age = int(request.POST.get('age'))
        disease = request.POST.get('disease')
        fees = int(request.POST.get('fees'))
        startMedsDate = request.POST.get('startMedsDate')
        doctoreName = request.POST.get('doctor')
        patientEntry = PatientDB.objects.get(id=id)
        try:
            patientEntry.firstName=fname 
            patientEntry.lastName=lname
            patientEntry.gender = gender
            patientEntry.age = age
            patientEntry.disease = disease
            patientEntry.doctorName = doctoreName
            patientEntry.doctorFees = fees
            patientEntry.startMedsDate = startMedsDate
            patientEntry.save()
            messages.add_message(request, messages.INFO, 'Patien Details Edited Successfully ')
        except:
            messages.add_message(request, messages.ERROR, 'Somthing gone wrong !! ')
        
        return render(request, 'patientList.html', {'patients': patients})

class deletePatient(View):
    def get(self, request):
        patients = PatientDB.objects.all()
        id = request.GET.get('id')
        patient = PatientDB.objects.get(id=id)
        try:
            patient.delete()
            messages.add_message(request, messages.INFO, 'Patien Details Deleted Successfully ')
        except:
            messages.add_message(request, messages.ERROR, 'Somthing gone wrong !! ')

        return render(request, 'patientList.html', {'patients': patients})
