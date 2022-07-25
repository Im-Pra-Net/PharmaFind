from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from pharmacydatabase.models import Brand, DrugType, Drug, DrugSet, Pharmacy

# Create your views here.

def testview(request):
    panadol = DrugType(name="panadol")
    panadol.save()
    return HttpResponse('This is a test page')