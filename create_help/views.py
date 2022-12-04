import json
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def create_help(request):
    request_body = json.loads(request.body)
    id = request_body.get('id')
    title = request_body.get('title')
    description = request_body.get('description')

    if title == None or description == None:
        return HttpResponseBadRequest("Title and Description must be filled")

    create_help_query = f"INSERT INTO help_ticket(id, title, description) \
        VALUES('{id}', '{title}', {description});"
    execute_query(create_help_query)

    return HttpResponse(status=201)