from rest_framework import serializers

from store.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand', 'brand_id']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color', 'color_id']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material', 'material_id']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'main_image', 'new_arrive', 'priceUAH', 'sale_priceUAH', 'sale']


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['main_category', 'url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'url']