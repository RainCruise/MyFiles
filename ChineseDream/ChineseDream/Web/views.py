#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from Web.models import Infomation_dars, Infomation_szqt
from django import forms
import re

# Create your views here.
def index(request):
    return render(request, 'Web/index.html')

def about_us(request):
    return render(request, 'Web/about_us.html')

def join_us_dars(request):   
    return render(request, 'Web/join_us_dars.html')

def join_us_dars_apply(request):
    name = request.POST['input_name']
    eamil_address = request.POST['input_email'] 
    number = request.POST['input_number']
    message = request.POST['input_message']
    Infomation_dars.objects.create(name=name, eamil_address=eamil_address, number=number, message_content=message)
    return render(request, 'Web/success.html')

def join_us_szqt(request):
    return render(request, 'Web/join_us_szqt.html')

def join_us_szqt_apply(request):
    name = request.POST['input_name']
    eamil_address = request.POST['input_email'] 
    number = request.POST['input_number']
    message = request.POST['input_message']
    Infomation_szqt.objects.create(name=name, eamil_address=eamil_address, number=number, message_content=message)
    return render(request, 'Web/success.html')
