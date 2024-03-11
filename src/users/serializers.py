from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Product
from django.contrib.auth.hashers import make_password

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',) 

class UserSerializer(serializers.ModelSerializer):
    favorite_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('favorite_products',)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'profile', ' favorite')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        User.objects.create(user=user)

        return user
