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
    
def insert_mat(id, mname, qty, units, d):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO MATERIAL VALUES({},'{}', {},'{}','{}')".format(id,mname, qty, units, d))

def delete_mat(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM MATERIAL WHERE MAT_ID = {}".format(id))

def update_mat(id, update):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE MATERIAL SET {} WHERE MAT_ID = {}".format(update, id))