# Generated by Django 4.0 on 2022-02-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_sex_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'men'), ('fomen', 'women'), ('unisex', 'unisex')], default='unisex', max_length=10),
        ),
    ]