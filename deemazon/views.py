from django.shortcuts import render
from django.http import HttpResponse
from . import views


def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')