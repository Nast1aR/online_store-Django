# Generated by Django 4.1 on 2024-03-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_brand_brand_alter_brand_brand_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_priceUAH',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
