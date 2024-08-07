# Generated by Django 5.0.7 on 2024-08-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystemapp', '0012_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]