from django.db import models

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=255, unique=True, verbose_name='Кольор')
    url = models.SlugField(unique=True, verbose_name='ID Кольору')

    def __str__(self):
        return self.color


class Material(models.Model):
    material = models.CharField(max_length=255, unique=True, verbose_name='Матеріал')
    url = models.SlugField(unique=True, verbose_name='ID Матеріалу')

    def __str__(self):
        return self.material


class Brand(models.Model):
    brand = models.CharField(max_length=255, unique=True, verbose_name='Бренд')
    logo = models.ImageField(upload_to='media/brand-logo/', blank=True, verbose_name='Логотип')
    url = models.SlugField(unique=True, verbose_name='ID Бренду')

    def __str__(self):
        return self.brand


class MainCategory(models.Model):
    main_category = models.CharField(max_length=255, unique=True, verbose_name='Основна Категорія')
    url = models.SlugField(unique=True, verbose_name='')

    def __str__(self):
        return self.main_category


class Category(models.Model):
    main_cat = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name='Основна Категорія')
    category = models.CharField(max_length=255, unique=True, verbose_name='Категорія')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.main_cat.main_category + '--' + self.category


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    sub_category = models.CharField(max_length=255, unique=True, verbose_name='ПідКатегорія')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.cat.main_cat.main_category + '--' + self.cat.category + '--' + self.sub_category


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    url = models.SlugField(unique=True)
    description = models.TextField()
    main_image = models.ImageField(upload_to='media/product_main_images/')
    total_quantity = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    product_type = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    new_arrive = models.BooleanField(default=True)
    priceUAH = models.PositiveSmallIntegerField()
    sale_priceUAH = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

    def sale(self):
        if self.sale_priceUAH == 0:
            return 0
        elif self.sale_priceUAH is None:
            return 0
        return self.priceUAH - self.sale_priceUAH

    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='media/product_images/')


class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)