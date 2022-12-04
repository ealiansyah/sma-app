import json
import jsonschema
from functools import wraps
from jsonschema import (
  Draft7Validator,
  draft7_format_checker,
)
from django.http import JsonResponse

# YES THIS THING SHOULD BE IN UTILITIES
def request_schema(schema, method='GET'):
  """
  Validate request based on given schema
  Based on given method will extract data from body or query string
  """
  validator = Draft7Validator(schema, format_checker=draft7_format_checker)

  def _func(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
      if request.method != method:
        return JsonResponse(status=400, data={'message': 'wrong method'})
      
      try:
        if request.method == 'GET':
          data = request.GET.copy()
        
        if request.method == 'POST':
          if request.content_type == 'application/json':
            # Handle json request
            if request.body == '':
              data = {}
            else:
              data = json.loads(request.body)
          elif request.content_type.startswith('application/x-www-form-urlencoded'):
            data = request.POST.copy()
          else:
            data = {}

        data.update(kwargs)
        kwargs.clear()
        
        validator.validate(data)
      except jsonschema.exceptions.ValidationError as ex:
        return JsonResponse(status=400, data={"error": ex.message})

      return func(request, data, *args, **kwargs)

    return wrapper

  return _func


from productCRUD.models import Product
from checkout.models import Checkout
from rest_framework.status import HTTP_400_BAD_REQUEST

def check_products_and_get_models(request, data):
  status = 200
  message = []

  productModels = []
  barcodes = []
  for product in data['products']:
    productModel = Product.objects.filter(barcode_id=product['barcode_id']).first()
    if productModel == None:
      status = HTTP_400_BAD_REQUEST
      message.append(f'Products with barcode_id {product["barcode_id"]} not found!')
    
    if product['barcode_id'] in barcodes:
      status = HTTP_400_BAD_REQUEST
      message.append(f'Found duplicates of products with barcode_id {product["barcode_id"]}!')
    barcodes.append(product['barcode_id'])

    productModels.append((productModel, product))

  return status, message, productModels

def create_and_apply_checkout(data, productModels):
  status = 200
  message = []
  checkout = Checkout()
  checkout.discount = data.get('discount', 0)
  checkout.save()

  # do operations
  for productModel, checkoutDetails in productModels:
    if productModel.quantity < checkoutDetails['quantity']:
      status = 209
      message.append(f'Products with barcode_id {checkoutDetails["barcode_id"]} only have {productModel.quantity}, but there is {checkoutDetails["quantity"]} in checkout!')

    productModel.quantity = max(0, productModel.quantity - checkoutDetails['quantity'])
    productModel.save()
    
    checkout.products_quantity.add(
      productModel.barcode_id, 
      through_defaults={
        'quantity': checkoutDetails['quantity'],
        'price': checkoutDetails['quantity'] * productModel.price,
      }
    )

  return status, message, checkout