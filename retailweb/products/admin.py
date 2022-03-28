from django.contrib import admin

from .models import Jackets, Pants, Product, Shoes, Clothes

admin.site.register(Product)
admin.site.register(Shoes)
admin.site.register(Jackets)
admin.site.register(Pants)
