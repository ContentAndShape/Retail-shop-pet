# Generated by Django 4.0 on 2022-01-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unisex', 'unisex')], default='unisex', max_length=10),
        ),
    ]
