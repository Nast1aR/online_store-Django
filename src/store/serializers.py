from rest_framework import serializers

from store.models import *


# Filters
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'url']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'url', 'col']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name', 'url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['type', 'url']


# ProductList
class ProductInventoryListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    url = serializers.SlugField(source='product.url')

    class Meta:
        model = ProductInventory
        fields = ['product_name', 'url', 'main_image', 'new_arrive', 'priceUAH', 'sale_priceUAH', 'sale']


# ProductDetail
class ProductInventoryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventoryImages
        fields = ['images']


class ProductInventoryAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventoryAttributes
        fields = ['attribute_type', 'value']


class ProductInventoryDetailSerializer(serializers.ModelSerializer):
    images = ProductInventoryImagesSerializer(many=True)
    attributes = ProductInventoryAttributesSerializer(many=True)

    class Meta:
        model = ProductInventory
        fields = [
            'sku',
            'color',
            'priceUAH', 'sale_priceUAH', 'sale',
            'new_arrive', 'images', 'attributes'
            ]


class ProductSerializer(serializers.ModelSerializer):
    inventory = ProductInventoryDetailSerializer(many=True)
    colors = ColorSerializer(many=True)
    product_type = serializers.CharField(source='product_type.type')

    class Meta:
        model = Product
        fields = ['product_name', 'url', 'description', 'product_type', 'colors', 'brand', 'inventory']
