from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'chemecardb/index.html')

def nav1(request):
    return render(request, 'chemecardb/nav1.html')

def roster(request):
    return HttpResponse('roster page')

def schedule(request):
    return HttpResponse('schedule page')

def materials(request):
    return HttpResponse('materials page')

def car(request):
    return HttpResponse('car page')