from django.db import models
from productCRUD.models import Product

# Create your models here.
class Checkout(models.Model):
  is_applied = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  products_quantity = models.ManyToManyField(Product, through='ProductQuantity')
  discount = models.PositiveIntegerField(default=0)
  
  class Meta:
    db_table = 'Checkout'
    ordering = ['created_at']

class ProductQuantity(models.Model):
  product_barcode = models.ForeignKey(Product, on_delete=models.CASCADE)
  checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  price = models.PositiveIntegerField()