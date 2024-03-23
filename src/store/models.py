from django.db import models

# Create your models here.


CATEGORY = [
    ('CA', 'Categories'),
    ('AC', 'Accessories'),
]


# Filters
class Color(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Кольор')
    url = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.col


class Material(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Матеріал')
    url = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.material


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Бренд')
    logo = models.ImageField(upload_to='media/brand-logo/', blank=True, verbose_name='Логотип')
    url = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.brand


# Categories
class ProductType(models.Model):
    category = models.CharField(max_length=2, choices=CATEGORY, verbose_name='Категорія')
    type = models.CharField(max_length=255, unique=True, verbose_name='Тип')
    url = models.SlugField(unique=True, verbose_name='URL')

    def __str__(self):
        return self.type


# All Product-tables
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True, verbose_name='Назва Продукту')
    url = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(related_name='Опис')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип Продукту')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name='Матерiал')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    colors = models.ManyToManyField(Color, verbose_name='Кольори')

    def __str__(self):
        return self.product_type + self.product_name


class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory', verbose_name='Продукт')
    sku = models.CharField(max_length=255, unique=True, verbose_name='Код Продукту')
    main_image = models.ImageField(upload_to='media/product_main_images/', verbose_name='Головне Фото')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='Кольор')
    quantity = models.PositiveIntegerField(verbose_name='Кiлькiсть')
    priceUAH = models.PositiveSmallIntegerField(verbose_name='Цiна')
    sale_priceUAH = models.PositiveSmallIntegerField(null=True, blank=True, default=0, verbose_name='Ціна зі знижкою')
    new_arrive = models.BooleanField(default=True, verbose_name='Нещодавно доданий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def sale(self):
        if self.sale_priceUAH == 0:
            return 0
        elif self.sale_priceUAH is None:
            return 0
        elif self.sale_priceUAH >= self.priceUAH:
            return ''
        return self.priceUAH - self.sale_priceUAH

    def __str__(self):
        return self.product.product_type.type + '--' + self.product


# Additional Product-tables
class ProductInventoryImages(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory, on_delete=models.CASCADE,
        related_name='images', verbose_name='Варіант Прдукту'
    )
    images = models.ImageField(upload_to='media/product_inventory_images/', verbose_name='Фото')


class ProductInventoryAttributes(models.Model):
    product = models.ForeignKey(
        ProductInventory, on_delete=models.CASCADE,
        related_name='attributes', verbose_name='Варіант Прдукту'
    )
    attribute_type = models.CharField(max_length=255, verbose_name='Тип атрибуту')
    value = models.CharField(max_length=255, verbose_name='Значення Атрибуту')