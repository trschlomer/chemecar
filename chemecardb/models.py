from django.db import models
from django.db import connection

# Create your models here.

def select_all(TABLE):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM {};".format(TABLE))
        row = cursor.fetchall()
    return row

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
        cursor.execute("INSERT INTO TRIAL VALUES({}, {}, {}, {}, {})".format(id, description,
        year))

def delete_trial(trial_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM TRIAL WHERE TRIAL_ID = {}".format(id))
        
