# Generated by Django 4.0 on 2022-02-12 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sex',
            new_name='gender',
        ),
    ]