# Generated by Django 4.1 on 2024-03-13 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_category_id_category_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='color_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='material_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='url',
        ),
    ]