from django.db import models

from retailweb.settings import BASE_DIR

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, default='No description')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    gender_choices = [
        ('men', 'men'),
        ('women', 'women'),
        ('unisex', 'unisex'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        default='unisex',
    )
    photo = models.ImageField(
        upload_to='products/', 
        default=str(BASE_DIR)+'/media/products/Null.jpg/',
        )

    def __str__(self):
        return self.name


class Shoes(Product):
    size_40_quantity = models.IntegerField(default=0)
    size_41_quantity = models.IntegerField(default=0)
    size_42_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Clothes(Product):
    Small_size_quantity = models.IntegerField(default=0)
    Medium_size_quantity = models.IntegerField(default=0)
    Large_size_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Jackets(Clothes):
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Pants(Clothes):
    leg_length = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
