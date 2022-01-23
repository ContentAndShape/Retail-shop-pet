from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, default='no description')
    collection = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category_choices = [
        ('boots', 'boots'),
        ('jackets', 'jackets'),
        ('pants', 'pants'),
        ('hats', 'hats'),
    ]
    category = models.CharField(max_length=15, choices=category_choices, default='no_category')
     

    def __str__(self):
        return self.name
