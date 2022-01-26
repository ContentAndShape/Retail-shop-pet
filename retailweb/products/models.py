from email.policy import default
from django.db import models

from retailweb.settings import BASE_DIR

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, default='no description')
    collection = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sex_choices = [
        ('male', 'male'),
        ('female', 'female'),
        ('unisex', 'unisex'),
    ]
    sex = models.CharField(
        max_length=10,
        choices=sex_choices,
        default='unisex',
    )
    category_choices = [
        ('boots', 'boots'),
        ('jackets', 'jackets'),
        ('pants', 'pants'),
        ('hats', 'hats'),
    ]
    category = models.CharField(
        max_length=15, 
        choices=category_choices, 
        default='no_category'
        )
    photo = models.ImageField(
        upload_to='products/', 
        default=BASE_DIR / 'media/products/Null.jpg/'
        )
     

    def __str__(self):
        return self.name
