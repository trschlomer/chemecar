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