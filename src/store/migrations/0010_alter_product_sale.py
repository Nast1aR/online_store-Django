# Generated by Django 4.1 on 2024-03-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
