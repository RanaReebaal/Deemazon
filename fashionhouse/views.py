from django.shortcuts import render
from django.http import HttpResponse
from . import views


def home(request):
    return render(request,'fashionhouse/home.html')


def index(request):
    return render(request,'fashionhouse/index.html')

