# Generated by Django 5.0.1 on 2024-02-26 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_subcategory_id_category_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='product_id',
        ),
    ]
