from django.shortcuts import render
from django.http import HttpResponse
from . import views


def home(request):
    return render(request,'jewelleryhouse/home.html')


def index(request):
    return render(request,'jewelleryhouse/index.html')

