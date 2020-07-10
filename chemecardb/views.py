from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
from .models import *
from django.db import *

# Create your views here.
def index(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM academic_year')
    years = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/index.html', {'years':years})

def insertyear(request):
    if request.method == 'POST':
        year_id = request.POST.get('textfield1', None)
        car_name = request.POST.get('textfield2', None)
        pow_name = request.POST.get('textfield3', None)
        stop_name = request.POST.get('textfield4', None)
        try:
           insert_year(year_id, car_name, pow_name, stop_name)
           table = select_all('academic_year')
           return render(request,'chemecardb/index.html', {'years':table})
        except ( OperationalError, ProgrammingError, IntegrityError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/index.html')

def nav1(request):
    return render(request, 'chemecardb/nav1.html')

def roster(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM roster')
    rosters = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/roster.html', {'rosters':rosters})

def rosterq(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT COMP_ID, ROLE FROM ROSTER WHERE YEAR_ID = 2018;')
    query1 = cursor.fetchall()
    cursor.execute('SELECT MEMBERS.COMP_ID, FNAME, LNAME FROM ROSTER, MEMBERS WHERE ROSTER.COMP_ID = MEMBERS.COMP_ID AND FOR_CREDIT = 1;')
    query2 = cursor.fetchall()
    cursor = db.cursor()
    cursor.execute('SELECT COMP_ID, FNAME, LNAME, ROLE, YEAR_ID FROM ROSTER JOIN MEMBERS USING (COMP_ID) GROUP BY ROLE ORDER BY YEAR_ID')
    query3 = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/rosterq.html', {'query1':query1, 'query2':query2, 'query3':query3})

def insertroster(request):
    if request.method == 'POST':
        year_id = request.POST.get('textfield1', None)
        comp_id = request.POST.get('textfield2', None)
        team = request.POST.get('textfield3', None)
        role = request.POST.get('textfield4', None)
        for_credit = request.POST.get('textfield5', None)
        try:
           insert_roster(year_id, comp_id, team, role, for_credit)
           table = select_all('roster')
           return render(request,'chemecardb/roster.html', {'rosters':table})
        except ( OperationalError, ProgrammingError, IntegrityError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/roster.html')

def deleteroster(request):
    if request.method == 'POST':
        comp_id = request.POST.get('textfield6', None)
        try:
           delete_roster(comp_id) 
           table = select_all('roster')
           return render(request,'chemecardb/roster.html', {'rosters':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/roster.html')

def updateroster(request):
    if request.method == 'POST':
        comp_id = request.POST.get('textfield7', None)
        update_text = request.POST.get('textfield8', None)
        try:
           update_roster(comp_id, update_text) 
           table = select_all('roster')
           return render(request,'chemecardb/roster.html', {'rosters':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/roster.html')


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
        date = request.POST.get('textfield1', None)
        description = request.POST.get('textfield2', None)
        year = request.POST.get('textfield3',None)
        try:
           insert_sched(sched_id, date, description, year)
           table = select_all('scheduling')
           return render(request,'chemecardb/scheduling.html', {'scheds':table})
        except (ProgrammingError,IntegrityError, OperationalError):
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
           table = select_all('scheduling')
           return render(request,'chemecardb/scheduling.html', {'scheds':table})
        except (IntegrityError):
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

def insertmats(request):
    if request.method == 'POST':
        mat_id = request.POST.get('textfield1', None)
        name = request.POST.get('textfield2', None)
        mat_qty = request.POST.get('textfield3', None)
        unit = request.POST.get('textfield4', None)
        descript = request.POST.get('textfield5', None)
        try:
           insert_mat(mat_id, name, mat_qty, unit, descript) 
           table = select_all('material')
           return render(request,'chemecardb/material.html', {'mats':table})
        except (IntegrityError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/material.html')

def deletemats(request):
    if request.method == 'POST':
        mat_id = request.POST.get('textfield6', None)
        try:
           delete_mat(mat_id) 
           table = select_all('material')
           return render(request,'chemecardb/material.html', {'mats':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/material.html')

def updatemats(request):
    if request.method == 'POST':
        mat_id = request.POST.get('textfield7', None)
        update_text = request.POST.get('textfield8', None)
        try:
           update_mat(mat_id, update_text) 
           table = select_all('material')
           return render(request,'chemecardb/material.html', {'mats':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/material.html')

def car(request):
    return render(request, 'chemecardb/car.html')

def powmech(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM pow_mech')
    pows = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/powmech.html', {'pows':pows})

def powmechq(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT POW_MECH.POW_ID, MATERIAL.MAT_ID, POW_QTY, NAME, YEAR_ID, POW_MECH.VOLTAGE*POW_MECH.CURRENT AS \'POWER\' FROM POW_SPEC, MATERIAL, POW_MECH WHERE POW_SPEC.POW_ID = POW_MECH.POW_ID AND MATERIAL.MAT_ID = POW_SPEC.MAT_ID ORDER BY POW_ID;')
    query1 = cursor.fetchall()
    cursor.execute('SELECT TRIAL_ID, POW_ID, PAYLOAD, DISTANCE, TRIAL_TIME FROM TRIAL WHERE DISTANCE = 10;')
    query2 = cursor.fetchall()
    cursor.execute('SELECT POW_ID, (VOLTAGE*CURRENT) / NUM_CELLS AS EFFICIENCY FROM POW_MECH ORDER BY EFFICIENCY DESC LIMIT 5;')
    query3 = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/powmechq.html', {'query1':query1, 'query2':query2, 'query3':query3})

def insertpows(request):
    if request.method == 'POST':
        year_id = request.POST.get('textfield0', None)
        pow_id = request.POST.get('textfield1', None)
        num_cells = request.POST.get('textfield2', None)
        voltage = request.POST.get('textfield3' , None)
        current = request.POST.get('textfield4' , None)
        try:
           insert_pow_mech(year_id, pow_id, num_cells, voltage, current) 
           table = select_all('pow_mech')
           return render(request,'chemecardb/powmech.html', {'pows':table})
        except (ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/powmech.html')

def deletepows(request):
    if request.method == 'POST':
        pow_id = request.POST.get('textfield5', None)
        try:
           delete_pow_mech(pow_id) 
           table = select_all('pow_mech')
           return render(request,'chemecardb/powmech.html', {'pows':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/powmech.html')


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
           insert_trial(pow_id, trial_id, payload, distance, trial_time) 
           table = select_all('trial')
           return render(request,'chemecardb/trial.html', {'trls':table})
        except (OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/scheduling.html')

def deletetrial(request):
    if request.method == 'POST':
        trial_id = request.POST.get('textfield5', None)
        try:
           delete_trial(trial_id) 
           table = select_all('trial')
           return render(request,'chemecardb/trial.html', {'trls':table})
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

def stopmechq(request):
    db = MySQLdb.connect(user='dbadmin', db='cheme_car_db', passwd='12345', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT STOP_ID, STOP_TIME FROM STOP_MECH WHERE STOP_TIME < 120 AND STOP_TIME > 100')
    query1 = cursor.fetchall()
    cursor.execute('SELECT STOP_ID, TRIAL_ID, TRIAL_TIME - STOP_TIME AS \'DELTA_T\' FROM (POW_MECH JOIN TRIAL USING(POW_ID)) JOIN STOP_MECH USING(YEAR_ID) WHERE ABS(TRIAL_TIME - STOP_TIME) <= 3')
    query2 = cursor.fetchall()
    db.close()
    return render(request, 'chemecardb/stopmechq.html', {'query1':query1, 'query2':query2})

def insertstops(request):
    if request.method == 'POST':
        stop_id = request.POST.get('textfield0', None)
        stop_time = request.POST.get('textfield1', None)
        year_id = request.POST.get('textfield2', None)
        try:
           insert_stop_mech(stop_id, stop_time, year_id) 
           table = select_all('stop_mech')
           return render(request,'chemecardb/stopmech.html', {'stops':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/stopmech.html')

def deletestops(request):
    if request.method == 'POST':
        stop_id = request.POST.get('textfield3', None)
        try:
           delete_stop_mech(stop_id) 
           table = select_all('stop_mech')
           return render(request,'chemecardb/stopmech.html', {'stops':table})
        except (IntegrityError, OperationalError, ProgrammingError):
            return HttpResponse("something went wrong! please hit the back button and try again...")
    else:
        return render(request, 'chemecardb/stopmech.html')
