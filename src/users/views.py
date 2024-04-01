from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FavoriteProducts
from .serializers import FavoriteProductsSerializer

class FavoriteProductsAPIView(APIView):
    def get(self, request):
        user = request.user
        favorite_products = FavoriteProducts.objects.filter(user=user)
        serializer = FavoriteProductsSerializer(favorite_products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            favorite_product = FavoriteProducts.objects.get(pk=pk)
        except FavoriteProducts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        favorite_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
