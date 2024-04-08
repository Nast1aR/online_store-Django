from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import FavoriteProductInventory
from .serializers import FavoriteProductInventorySerializer

class AddFavoriteProductTypesView(generics.CreateAPIView):
    serializer_class = FavoriteProductInventorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RemoveFavoriteProductTypesView(generics.DestroyAPIView):
    queryset = FavoriteProductInventory.objects.all()
    serializer_class = FavoriteProductInventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class ListFavoriteProductTypessView(generics.ListAPIView):
    serializer_class = FavoriteProductInventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteProductInventory.objects.filter(user=self.request.user)
