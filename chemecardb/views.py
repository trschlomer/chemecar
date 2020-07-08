from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

# Create your views here.

def index(request):
    return render(request, 'chemecardb/index.html')

def nav1(request):
    return render(request, 'chemecardb/nav1.html')

def roster(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM roster')
    rosters = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/roster.html', {'rosters':rosters})

def members(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM members')
    mems = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/members.html', {'mems':mems})
    
def scheduling(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM scheduling')
    scheds = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/scheduling.html', {'scheds':scheds})

def material(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM material')
    mats = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/material.html', {'mats':mats})

def car(request):
    return render(request, 'chemecardb/car.html')

def powmech(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM pow_mech')
    pows = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/powmech.html', {'pows':pows})

def trial(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM trial')
    trls = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/trial.html', {'trls':trls})

def stopmech(request):
    db = MySQLdb.connect(user='simran', db='cheme_car_db', passwd='Orange123', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stop_mech')
    stops = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/stopmech.html', {'stops':stops})
