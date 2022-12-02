from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    quantity = models.PositiveIntegerField(default=0)
    barcode_id = models.CharField(primary_key=True, max_length=127)
    image = models.FileField(upload_to='documents/', null=True)
    # TODO: Product_Category as foreign key

    def __str__(self):
        return self.name