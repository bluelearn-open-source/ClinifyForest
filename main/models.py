from django.db import models

# Create your models here.
class Store(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_desc = models.CharField(max_length=200)
    item_stock = models.IntegerField()

    def __str__(self):
        return self.item_name