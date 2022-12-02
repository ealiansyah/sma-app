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

        create_product_query = f"INSERT INTO product(name, description, quantity, barcode_id) \
            VALUES('{name}', '{description}', {quantity}, '{barcode_id}');"
        execute_query(create_product_query)

        return HttpResponse(status=201)

    return HttpResponseNotAllowed(permitted_methods=['POST'])

@csrf_exempt
def get_product(request):
    if(request.method == 'GET'):
        name = request.GET.get('name', '')

        get_product_query = f"SELECT * FROM product WHERE name LIKE '%{name}%';"
        products = execute_and_fetchall_query(get_product_query)
        products = json.dumps(products)

        return HttpResponse(products)

    return HttpResponseNotAllowed(permitted_methods=['GET'])

@csrf_exempt
def update_product(request):
    if(request.method == 'POST'):
        request_body = json.loads(request.body)
        name = request_body.get("name")
        description = request_body.get("description")
        quantity = request_body.get("quantity")
        barcode_id = request_body.get("barcode_id")

        if barcode_id == None:
            return HttpResponseBadRequest("Barcode id can't be null")

        update_product_query = "UPDATE product "
        if name != None:
            update_product_query += f"SET name = '{name}', "
        if description != None:
            update_product_query += f"SET description = '{description}', "
        if quantity != None:
            update_product_query += f"SET quantity = {quantity}, "

        update_product_query = update_product_query[:-2]
        update_product_query += f" WHERE barcode_id = '{barcode_id}';"
        execute_query(update_product_query)

        return HttpResponse(status=200)

    return HttpResponseNotAllowed(permitted_methods=['POST'])


def execute_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def execute_and_fetchall_query(query):
    result = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = dictfetchall(cursor)
    return result

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]