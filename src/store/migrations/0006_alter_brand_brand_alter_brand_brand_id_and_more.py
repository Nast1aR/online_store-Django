# Generated by Django 4.1 on 2024-03-07 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_url_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=255, unique=True, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.SlugField(unique=True, verbose_name='ID Бренду'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media/brand-logo/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=255, unique=True, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='category',
            name='main_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.maincategory', verbose_name='Основна Категорія'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=255, unique=True, verbose_name='Кольор'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color_id',
            field=models.SlugField(unique=True, verbose_name='ID Кольору'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='main_category',
            field=models.CharField(max_length=255, unique=True, verbose_name='Основна Категорія'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='main_category_id',
            field=models.SlugField(unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='material',
            name='material',
            field=models.CharField(max_length=255, unique=True, verbose_name='Матеріал'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_id',
            field=models.SlugField(unique=True, verbose_name='ID Матеріалу'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(max_length=255, unique=True, verbose_name='ПідКатегорія'),
        ),
    ]
