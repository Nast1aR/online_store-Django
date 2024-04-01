from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User, FavoriteProducts
from django.contrib.auth.hashers import make_password
# from store.serializers import ProductListSerializer


class FavoriteProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProducts
        fields = ('id', 'user', 'product', 'added_at')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    favorite_products = FavoriteProductsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'favorite')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hashed_password = make_password(password)
        user = User.objects.create(**validated_data, password=hashed_password)
        return user
    