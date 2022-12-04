from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.db import connection

# Create your views here.


# test query dari postgresql railway
def home(request):
    query = "SELECT * FROM test"
    result = execute_query(query)
    print(result)
    return render(request, 'home.html')


# buat execute query dari postgresql
def execute_query(query):
    result = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result