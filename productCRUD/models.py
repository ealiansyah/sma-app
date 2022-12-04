from django.db import models

class Product_Category(models.Model):
    nama_kategori = models.CharField(primary_key=True, max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_kategori

class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    barcode_id = models.CharField(primary_key=True, max_length=127)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
