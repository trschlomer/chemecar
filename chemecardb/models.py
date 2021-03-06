from django.db import models
from django.db import connection

# Create your models here.

def select_all(TABLE):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM {};".format(TABLE))
        row = cursor.fetchall()
    return row

def insert_year(id, car_name, pow_name, stop_name):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO ACADEMIC_YEAR VALUES({},'{}','{}','{}')".format(id,car_name,
        pow_name, stop_name))

def insert_mem(id, fname, lname, major, grad_year):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO MEMBERS VALUES('{}','{}','{}','{}',{})".format(id,fname,
        lname, major, grad_year))

def delete_mem(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM MEMBERS WHERE COMP_ID = '{}'".format(id))

def update_mem(id, update):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE MEMBERS SET {} WHERE COMP_ID = '{}'".format(update, id))
    
def insert_mat(id, mname, qty, units, d):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO MATERIAL VALUES({},'{}', {},'{}','{}')".format(id,mname, qty, units, d))

def delete_mat(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM MATERIAL WHERE MAT_ID = {}".format(id))

def update_mat(id, update):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE MATERIAL SET {} WHERE MAT_ID = {}".format(update, id))
        
def insert_roster(year_id, comp_id, team, role, for_credit):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO ROSTER VALUES({},'{}','{}','{}',{})".format(year_id,comp_id,
        team, role, for_credit))

def delete_roster(comp_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM ROSTER WHERE COMP_ID = '{}'".format(comp_id))

def update_roster(comp_id, update):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE ROSTER SET {} WHERE COMP_ID = '{}'".format(update, comp_id))
    
def insert_sched(id, date, description, year):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO SCHEDULING VALUES({},'{}', '{}', {})".format(id, date,
        description, year))

def delete_sched(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM SCHEDULING WHERE SCHED_ID = {}".format(id))

def update_sched(id, update):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE SCHEDULING SET {} WHERE SCHED_ID = {}".format(update, id))
        
def insert_trial(trial_id, pow_id, payload, distance, trial_time):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO TRIAL VALUES({}, {}, {}, {}, {})".format(trial_id, pow_id, payload,
        distance, trial_time))

def delete_trial(trial_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM TRIAL WHERE TRIAL_ID = {}".format(trial_id))
        
def insert_stop_mech(stop_id, stop_time, year_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO STOP_MECH VALUES({}, {}, {})".format(stop_id, stop_time,
        year_id))

def delete_stop_mech(stop_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM STOP_MECH WHERE STOP_ID = {}".format(stop_id))
        
def insert_pow_mech(year_id, pow_id, num_cells, voltage, current):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO POW_MECH VALUES({}, {}, {}, {}, {})".format(year_id, pow_id,
        num_cells, voltage, current))

def delete_pow_mech(pow_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM POW_MECH WHERE POW_ID = {}".format(pow_id))
