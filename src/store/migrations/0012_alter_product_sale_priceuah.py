# Generated by Django 4.1 on 2024-03-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_sale_product_sale_priceuah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_priceUAH',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]