import json
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_product(request):
    if(request.method == 'POST'):
        request_body = json.loads(request.body)
        name = request_body.get("name")
        description = request_body.get("description", "")
        quantity = request_body.get("quantity", 0)
        barcode_id = request_body.get("barcode_id")

        if barcode_id == None  or  name == None:
            return HttpResponseBadRequest("Barcode id and name can't be null")

        create_table_query = "CREATE TABLE IF NOT EXISTS product (\
            name VARCHAR(63) not null, \
            description VARCHAR(127), \
            quantity INT default 0, \
            barcode_id VARCHAR(127) primary key \
        );"
        execute_query(create_table_query)

        create_product_query = f"INSERT INTO product(name, description, quantity, barcode_id) \
            VALUES('{name}', '{description}', {quantity}, '{barcode_id}');"
        execute_query(create_product_query)

        return HttpResponse(status=201)

    return HttpResponseNotAllowed(permitted_methods=['POST'])

def execute_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
