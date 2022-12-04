from django.db import models
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)

class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    quantity = models.PositiveIntegerField(default=0)
    barcode_id = models.CharField(primary_key=True, max_length=127)
    # TODO: Product_Category as foreign key

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"