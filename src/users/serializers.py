from rest_framework import serializers
from .models import FavoriteProductInventory, User 

class FavoriteProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProductInventory
        fields = ('id', 'user', 'product', 'added_at')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    favorite_products = FavoriteProductInventorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'favorite_products')
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user