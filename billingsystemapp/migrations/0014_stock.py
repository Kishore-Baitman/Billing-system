# Generated by Django 5.0.7 on 2024-08-01 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystemapp', '0013_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingsystemapp.category')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingsystemapp.product')),
            ],
        ),
    ]
