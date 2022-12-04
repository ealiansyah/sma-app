from django.db import models
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)

class Product_Category(models.Model):
    nama_kategori = models.CharField(primary_key=True, max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_kategori

    class Meta:
        db_table = "product_category"

class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    barcode_id = models.CharField(primary_key=True, max_length=127)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, db_column='category')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"