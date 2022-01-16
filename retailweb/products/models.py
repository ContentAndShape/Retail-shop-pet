from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    collection = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_boots = models.BooleanField(default=0)
    is_pants = models.BooleanField(default=0)
    is_hats = models.BooleanField(default=0)
    is_jackets = models.BooleanField(default=0)
     

    def __str__(self):
        return self.name
