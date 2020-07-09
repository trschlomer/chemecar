from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
from .models import *
from django.db import *

# Create your views here.

#def index(request):
#    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
#    cursor = db.cursor()
#    cursor.execute('SELECT * FROM academic_year')
#    years = cursor.fetchall()
#    db.close()
#    return render(request, 'chemecardb/form.html', {'years':years})

#def search(request):
#    if request.method == 'POST':
#        search_id = request.POST.get('textfield', None)
#        try:
#           table = select_all(search_id)
#           return render(request,'chemecardb/index.html', {'years':table})
#        except ProgrammingError:
#            return HttpResponse("no such table, please hit the back button and try again")
#    else:
#        return render(request, 'chemecardb/form.html')


def index(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM academic_year')
    years = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/index.html', {'years':years})

def nav1(request):
    return render(request, 'chemecardb/nav1.html')

def roster(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM roster')
    rosters = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/roster.html', {'rosters':rosters})

def members(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM members')
    mems = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/members.html', {'mems':mems})
    
def insertmems(request):
    if request.method == 'POST':
        comp_id = request.POST.get('textfield1', None)
        fname = request.POST.get('textfield2', None)
        lname = request.POST.get('textfield3', None)
        major = request.POST.get('textfield4', None)
        grad_year = request.POST.get('textfield5', None)
        try:
           insert_mem(comp_id, fname, lname, major, grad_year) 
           table = select_all('members')
           return render(request,'chemecardb/members.html', {'mems':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/members.html')

def deletemems(request):
    if request.method == 'POST':
        comp_id = request.POST.get('textfield6', None)
        try:
           delete_mem(comp_id) 
           table = select_all('members')
           return render(request,'chemecardb/members.html', {'mems':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/members.html')

def updatemems(request):
    if request.method == 'POST':
        comp_id = request.POST.get('textfield7', None)
        update_text = request.POST.get('textfield8', None)
        try:
           update_mem(comp_id, update_text) 
           table = select_all('members')
           return render(request,'chemecardb/members.html', {'mems':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/members.html')

def scheduling(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM scheduling')
    scheds = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/scheduling.html', {'scheds':scheds})

def insertsched(request):
    if request.method == 'POST':
        sched_id = request.POST.get('textfield0', None)
        description = request.POST.get('textfield1', None)
        date = request.POST.get('textfield2', None)
        try:
           insert_sched(sched_id, description, date) 
           table = select_all('schedule')
           return render(request,'chemecardb/scheduling.html', {'scheds':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/scheduling.html')

def deletesched(request):
    if request.method == 'POST':
        sched_id = request.POST.get('textfield6', None)
        try:
           delete_sched(sched_id) 
           table = select_all('scheduling')
           return render(request,'chemecardb/scheduling.html', {'scheds':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/scheduling.html')

def updatesched(request):
    if request.method == 'POST':
        sched_id = request.POST.get('textfield7', None)
        update_text = request.POST.get('textfield8', None)
        try:
           update_sched(sched_id, update_text) 
           table = select_all('members')
           return render(request,'chemecardb/scheduling.html', {'sched':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/scheduling.html')

def material(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM material')
    mats = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/material.html', {'mats':mats})

def car(request):
    return render(request, 'chemecardb/car.html')

def powmech(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM pow_mech')
    pows = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/powmech.html', {'pows':pows})

def trial(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM trial')
    trls = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/trial.html', {'trls':trls})

def inserttrial(request):
    if request.method == 'POST':
        trial_id = request.POST.get('textfield0', None)
        pow_id = request.POST.get('textfield1', None)
        payload = request.POST.get('textfield2', None)
        distance = request.POST.get('textfield3', None)
        trial_time = request.POST.get('textfield4', None)
        try:
           insert_trial(trial_id, pow_id, payload, distance, trial_time) 
           table = select_all('trial')
           return render(request,'chemecardb/trial.html', {'scheds':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/scheduling.html')

def deletetrial(request):
    if request.method == 'POST':
        trial_id = request.POST.get('textfield5', None)
        try:
           delete_trial(trial_id) 
           table = select_all('trial')
           return render(request,'chemecardb/trial.html', {'trial':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/trial.html')

def stopmech(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stop_mech')
    stops = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/stopmech.html', {'stops':stops})
