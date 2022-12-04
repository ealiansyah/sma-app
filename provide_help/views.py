import json
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["GET"])
def get_help_list(request):

    get_help_query = f"SELECT * FROM help_ticket';"
    help_list = execute_and_fetchall_query(get_help_query)
    help_list = json.dumps(help_list)

    return HttpResponse(help_list)

@csrf_exempt
@require_http_methods(["POST"])
def provide_help(request):
    request_body = json.loads(request.body)
    id = request_body.get('id')
    response = request_body.get('response')

    if response == None:
        return HttpResponseBadRequest("Response must not be null")
    
    provide_help_query = f"UPDATE help_ticket SET response = '{response}' \
        WHERE id = '{id}';"
    execute_query(provide_help_query)

    return HttpResponse(201)

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