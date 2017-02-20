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
    if(request.method == 'POST'):
        request_post = str(request.POST)
        #print("request " + request_post)
        mode = re.compile(r"\'.*?\'")
        strs = mode.findall(request_post)
        if strs:
            #if strs is not None:
            mode = re.compile(r"/NAME:.*?\:NAME/")
            r = mode.findall(str(strs[1]))[0]
            name = r[6:-6]

            mode = re.compile(r"/EMAIL:.*?\:EMAIL/")
            r = mode.findall(str(strs[1]))[0]
            eamil_address = r[7:-7]

            mode = re.compile(r"/NUMBER:.*?\:NUMBER/")
            r = mode.findall(str(strs[1]))[0]
            number = r[8:-8]

            mode = re.compile(r"/MESSAGE:.*?\:MESSAGE/")
            r = mode.findall(str(strs[1]))[0]
            message = r[9:-9]

            Infomation_dars.objects.create(name=name, eamil_address=eamil_address, number=number, message_content=message)
            
    return render(request, 'Web/join_us_dars.html')

def join_us_szqt(request):
    if(request.method == 'POST'):
        request_post = str(request.POST)
        #print("request " + request_post)
        mode = re.compile(r"\'.*?\'")
        strs = mode.findall(request_post)
        if strs:
            #if strs is not None:
            mode = re.compile(r"/NAME:.*?\:NAME/")
            r = mode.findall(str(strs[1]))[0]
            name = r[6:-6]

            mode = re.compile(r"/EMAIL:.*?\:EMAIL/")
            r = mode.findall(str(strs[1]))[0]
            eamil_address = r[7:-7]

            mode = re.compile(r"/NUMBER:.*?\:NUMBER/")
            r = mode.findall(str(strs[1]))[0]
            number = r[8:-8]

            mode = re.compile(r"/MESSAGE:.*?\:MESSAGE/")
            r = mode.findall(str(strs[1]))[0]
            message = r[9:-9]

            Infomation_szqt.objects.create(name=name, eamil_address=eamil_address, number=number, message_content=message)

    return render(request, 'Web/join_us_szqt.html')
