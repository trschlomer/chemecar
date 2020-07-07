from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

# Create your views here.

def index(request):
    return render(request, 'chemecardb/index.html')

def nav1(request):
    return render(request, 'chemecardb/nav1.html')

def roster(request):
    return render(request, 'chemecardb/roster.html')

def members(request):
    return render(request, 'chemecardb/members.html')
    
def scheduling(request):
    return render(request, 'chemecardb/scheduling.html')

def material(request):
    #change this
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM material')
    mats = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/material.html', {'mats':mats})

def car(request):
    return render(request, 'chemecardb/car.html')

def powmech(request):
    return render(request, 'chemecardb/powmech.html')

def trial(request):
    #change this
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM trial')
    trls = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/trial.html', {'trls':trls})

def stopmech(request):
    return render(request, 'chemecardb/stopmech.html') 
