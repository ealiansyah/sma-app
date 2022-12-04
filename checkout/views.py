from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from checkout.models import ProductQuantity

from checkout.serializers import CheckoutSerializer, ProductQuantitySerializer

from .utils import request_schema
from . import schema, utils

from productCRUD.models import Product
from productCRUD.serializers import ProductSerializer

SEARCH_TYPE = ['barcode_id', 'name']

@csrf_exempt
@api_view(['GET'])
@request_schema(schema.search_request, method='GET')
def search_products(request, data):
  search_type = data['search_type']
  payload = data['payload']

  if search_type not in SEARCH_TYPE:
    return HttpResponseBadRequest(f'Search type {search_type} not found!')

  filter_kwargs = {
    f'{search_type}__icontains': payload
  }

  products = Product.objects.filter(**filter_kwargs)
  serializer = ProductSerializer(products, many=True)

  return Response(status=200, data=serializer.data)
  # return JsonResponse(status=200, data=serialized_products)


@csrf_exempt
@api_view(['POST'])
@request_schema(schema.checkout_request, method='POST')
def post_checkout(request, data):  
  # check every product exist in checkout
  status, message, productModels = utils.check_products_and_get_models(request, data)

  if status // 100 != 2:
    # non accepted codes
    return JsonResponse(status=status, data={ 'message': message })

  status, message, checkout = utils.create_and_apply_checkout(data, productModels)

  jsonData = CheckoutSerializer(checkout).data

  return JsonResponse(status=status, data={ 'message': message, 'data': jsonData })