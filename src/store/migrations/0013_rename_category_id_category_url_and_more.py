# Generated by Django 4.1 on 2024-03-12 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_sale_priceuah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='maincategory',
            old_name='main_category_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='subcategory_id',
            new_name='url',
        ),
    ]
