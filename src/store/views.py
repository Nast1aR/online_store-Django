from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import *
from store.serializers import *


# Filters
class BrandAPIView(APIView):
    def get(self, *args):
        model = Brand.objects.all()
        serializer_model = BrandSerializer(model, many=True)
        return Response(serializer_model.data)


class ColorAPIView(APIView):
    def get(self, *args):
        model = Color.objects.all()
        serializer_model = ColorSerializer(model, many=True)
        return Response(serializer_model.data)


class MaterialAPIView(APIView):
    def get(self, *args):
        model = Material.objects.all()
        serializer_model = MaterialSerializer(model, many=True)
        return Response(serializer_model.data)


# Categories
class CategoriesListAPIView(APIView):
    def get(self, *args):
        model = ProductType.objects.filter(category='CA')
        serializer_model = CategorySerializer(model, many=True)
        return Response(serializer_model.data)


class AccessoriesListAPIView(APIView):
    def get(self, *args):
        model = ProductType.objects.filter(category='AC')
        serializer_model = CategorySerializer(model, many=True)
        return Response(serializer_model.data)


# MainPage
class ProductMainOnSaleAPIView(APIView):
    def get(self, *args):
        model = ProductInventory.objects.order_by('product', '-id').distinct('product')[:8]
        serializer_model = ProductInventoryListSerializer(model, many=True)
        return Response(serializer_model.data)


class ProductMainNewArrivesAPIView(APIView):
    def get(self, *args):
        model = ProductInventory.objects.filter(new_arrive=True).order_by('product', '-id').distinct('product')[:8]
        serializer_model = ProductInventoryListSerializer(model, many=True)
        return Response(serializer_model.data)


# ProductDetail
class ProductDetailAPIView(APIView):
    def get(self, request, query):
        model = Product.objects.get(url=query)
        model_serializer = ProductSerializer(model)
        return Response(model_serializer.data)

