from django.db import models
from provider.models import Kitchen
# Create your models here.

class Menu(models.Model):

    kitchenID = models.ForeignKey(Kitchen,on_delete=models.CASCADE)
    title = models.CharField()
    total = models.DecimalField(decimal_places=2, max_digits= 100)




