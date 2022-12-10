import json
from django.http import HttpResponseBadRequest, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def create_product(request):
    request_body = json.loads(request.body)
    name = request_body.get("name")
    description = request_body.get("description", "")
    quantity = request_body.get("quantity", 0)
    barcode_id = request_body.get("barcode_id")
    price = request_body.get("price", 0)
    category = request_body.get("category")

    if barcode_id == None  or  name == None  or  category == None:
        return HttpResponseBadRequest("Barcode id, name, and category can't be null")

    create_product_query = f"INSERT INTO product(name, description, quantity, barcode_id, price, category) \
        VALUES('{name}', '{description}', {quantity}, '{barcode_id}', {price}, '{category}');"
    execute_query(create_product_query)

    return HttpResponse(status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_product(request):
    name = request.GET.get('name', '')

    get_product_query = f"SELECT * FROM product WHERE name LIKE '%{name}%';"
    products = execute_and_fetchall_query(get_product_query)
    products = json.dumps(products)

    return HttpResponse(products)

@csrf_exempt
@require_http_methods(["POST"])
def update_product(request):
    request_body = json.loads(request.body)
    name = request_body.get("name")
    description = request_body.get("description")
    quantity = request_body.get("quantity")
    barcode_id = request_body.get("barcode_id")
    price = request_body.get("price")
    category = request_body.get("category")

    if barcode_id == None:
        return HttpResponseBadRequest("Barcode id can't be null")

    update_product_query = "UPDATE product SET"
    if name != None:
        update_product_query += f" name = '{name}', "
    if description != None:
        update_product_query += f" description = '{description}', "
    if quantity != None:
        update_product_query += f" quantity = {quantity}, "
    if price != None:
        update_product_query += f" price = {price}, "
    if category != None:
        update_product_query += f" category = '{category}', "

    update_product_query = update_product_query[:-2]
    update_product_query += f" WHERE barcode_id = '{barcode_id}';"
    execute_query(update_product_query)

    return HttpResponse(status=200)

@csrf_exempt
@require_http_methods(["POST"])
def delete_product(request):
    request_body = json.loads(request.body)
    barcode_id = request_body.get("barcode_id")

    if barcode_id == None:
        return HttpResponseBadRequest("Barcode id can't be null")

    delete_product_query = f"DELETE FROM product WHERE barcode_id = '{barcode_id}';"
    execute_query(delete_product_query)

    return HttpResponse(status=200)


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
