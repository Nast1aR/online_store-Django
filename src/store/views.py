from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import *
from store.serializers import *


# Filters
class BrandAPIView(APIView):
    def get_brands(self, *args):
        model = Brand.objects.all()
        serializer_model = BrandSerializer(model, many=True)
        return Response(serializer_model.data)


class ColorAPIView(APIView):
    def get_colors(self, *args):
        model = Color.objects.all()
        serializer_model = ColorSerializer(model, many=True)
        return Response(serializer_model.data)


class MaterialAPIView(APIView):
    def get_materials(self, *args):
        model = Material.objects.all()
        serializer_model = MaterialSerializer(model, many=True)
        return Response(serializer_model.data)


# Categories
class CategoriesListAPIView(APIView):
    def get_categories(self, *args):
        model = ProductType.objects.filter(cat_type='CA')
        serializer_model = CategorySerializer(model, many=True)
        return Response(serializer_model.data)


class AccessoriesListAPIView(APIView):
    def get_accessories(self, *args):
        model = ProductType.objects.filter(cat_type='AC')
        serializer_model = CategorySerializer(model, many=True)
        return Response(serializer_model.data)


# MainPage
class ProductMainOnSaleAPIView(APIView):
    def get_product_main_on_sale(self, *args):
        model = ProductInventory.objects.distinct('product').order_by('-id')[:8]
        serializer_model = ProductInventoryListSerializer(model, many=True)
        return Response(serializer_model.data)


class ProductMainNewArrivesAPIView(APIView):
    def get_product_main_new_arrives(self, *args):
        model = ProductInventory.objects.filter(new_arrive=True).distinct('product').order_by('-id')[:8]
        serializer_model = ProductInventoryListSerializer(model, many=True)
        return Response(serializer_model.data)


# ProductDetail
class ProductDetailAPIView(APIView):
    def get_product_detail(self, query):
        model = Product.objects.get(url=query)
        model_serializer = ProductSerializer(model)
        return Response(model_serializer.data)

