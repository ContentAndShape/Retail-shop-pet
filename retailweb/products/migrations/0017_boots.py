# Generated by Django 4.0 on 2022-02-28 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boots',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('size', models.IntegerField(choices=[('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46')], max_length=4)),
            ],
            bases=('products.product',),
        ),
    ]
