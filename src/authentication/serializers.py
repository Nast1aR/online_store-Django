# from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
# from users.models import User
# from .models import Profile


# class UserTokenSerializer(serializers.Serializer):
#     access_token = serializers.CharField()
#     refresh_token = serializers.CharField()

#     # def __init__(self, *args, **kwargs):
#     #     super(UserTokenSerializer, self).__init__(*args, **kwargs)

#     # def create(self, validated_data):
#     #     pass

#     # def update(self, instance, validated_data):
#     #     pass
#     def get_access_token(self, obj):
#         return obj.get('access_token')

#     def get_refresh_token(self, obj):
#         return obj.get('refresh_token')

# # class UserRegisterSerializer(serializers.ModelSerializer):
# #     # password = serializers.CharField(write_only=True)
# #     # password2 = serializers.CharField(write_only=True)
# #     class Meta:
# #         model = User
# #         fields = ['first_name', 'last_name','email',"phone_number" 'password', "password2"]

# #     def create(self, validated_data):
# #         password = validated_data.pop('password')
# #         password2 = validated_data.pop('password2')
# #         if password != password2:
# #             raise serializers.ValidationError("Passwords do not match")
# #         user = User.objects.create_user(**validated_data)
# #         user.set_password(password)
# #         user.save()
# #         return user

        
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'


# class UserRegisterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('name', 'email', 'password')
        
#     name = serializers.CharField(max_length=255, required=True)
    
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())],
#         )
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#         style={'input_type': 'password'},
#         validators=[validate_password],
#         )

        

#     def create(self, validated_data):
#         name = validated_data.pop('name')
        
        
#         #create a new user with validated data
#         user = User.objects.create_user(
#             validated_data['email'],
#             )
        
#         #Set the hashed password for the user and save profile object
#         user.set_password(validated_data['password'])
#         user.save()
        
        
#         #create a new profile object linked to the user
#         profile = Profile.objects.create(
#             user=user,
#             name=name
#             )
#         profile.save()

        
#         return user

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#     access_token = serializers.CharField(read_only=True)
#     refresh_token = serializers.CharField(read_only=True)

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if not email or not password:
#             raise serializers.ValidationError("Must include 'email' and 'password'", code='authentication')

#         user = User.objects.filter(email=email).first()
#         if not user or not user.check_password(password):
#             raise serializers.ValidationError("Unable to log in with provided credentials.", code='authentication')

#         refresh = RefreshToken.for_user(user)
#         attrs['access_token'] = str(refresh.access_token)
#         attrs['refresh_token'] = str(refresh)
#         return attrs


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name','email',"phone_number"]

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from .models import Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def get_access_token(self, obj):
        return obj.get('access_token')

    def get_refresh_token(self, obj):
        return obj.get('refresh_token')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def create(self, validated_data):
        name = validated_data.pop('name')
        user = User.objects.create_user(validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(user=user, name=name)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Must include 'email' and 'password'", code='authentication')

        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError("Unable to log in with provided credentials.", code='authentication')

        refresh = RefreshToken.for_user(user)
        attrs['access_token'] = str(refresh.access_token)
        attrs['refresh_token'] = str(refresh)
        return attrs
