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
        category_arr = {
            self.is_boots: 'boots',
            self.is_pants: 'pants',
            self.is_hats: 'hats',
            self.is_jackets: 'jackets',
        }
        
        for i in category_arr:
            if i == 1:
                return f'name: {self.name}, category: {category_arr[i]}'

        return f'name: {self.name}, category: no'
