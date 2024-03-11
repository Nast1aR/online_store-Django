from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import *
from store.serializers import *


class ColorAPIView(APIView):
    def get(self, *args):
        model = Color.objects.all()
        serializer_model = ColorSerializer(model, many=True)
        return Response(serializer_model.data)


class BrandAPIView(APIView):
    def get(self, *args):
        model = Brand.objects.all()
        serializer_model = BrandSerializer(model, many=True)
        return Response(serializer_model.data)


class MaterialAPIView(APIView):
    def get(self, *args):
        model = Material.objects.all()
        serializer_model = MaterialSerializer(model, many=True)
        return Response(serializer_model.data)


class ProductMainOnSaleAPIView(APIView):
    def get(self, *args):
        model = Product.objects.order_by('-id')[:8]
        serializer_model = ProductListSerializer(model, many=True)
        return Response(serializer_model.data)


class ProductMainNewArrivesAPIView(APIView):
    def get(self, *args):
        model = Product.objects.filter(new_arrive=True).order_by('-id')[:8]
        serializer_model = ProductListSerializer(model, many=True)
        return Response(serializer_model.data)


