from .models import Checkout, ProductQuantity
from rest_framework import serializers

class ProductQuantitySerializer(serializers.ModelSerializer):
  product_barcode = serializers.ReadOnlyField(source='product_barcode.barcode_id')

  class Meta:
    model = ProductQuantity
    fields = ('product_barcode', 'quantity')

class CheckoutSerializer(serializers.ModelSerializer):
  products_quantity = ProductQuantitySerializer(source='productquantity_set', read_only=True, many=True)

  class Meta:
    model = Checkout
    fields = '__all__'
