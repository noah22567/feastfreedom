from django.db import models
from provider.models import Kitchen
# Create your models here.

# class Menu(models.Model):
#
#     kitchenID = models.ForeignKey(Kitchen,on_delete=models.CASCADE)
#     title = models.CharField()
#     total = models.DecimalField(decimal_places=2, max_digits= 100)
#


class MenuItem(models.Model):
    name = models.CharField(max_length=64, blank=True, null=False)
    is_veg = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

