# Generated by Django 5.0.7 on 2024-07-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystemapp', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='purchasetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='expirydate',
            field=models.DateField(null=True),
        ),
    ]