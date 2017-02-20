#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Web/index.html')

def about_us(request):
    return render(request, 'Web/about_us.html')

def join_us_dars(request):
    return render(request, 'Web/join_us_dars.html')

def join_us_szqt(request):
    return render(request, 'Web/join_us_szqt.html')
