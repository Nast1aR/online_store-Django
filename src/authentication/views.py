from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from .serializers import UserRegisterSerializer, UserLoginSerializer, ProfileSerializer
from users.serializers import UserSerializer



class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(tokens, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        serializer = UserRegisterSerializer()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        serializer = UserRegisterSerializer()
        return Response(serializer.data)
    

class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)



class ProfileUpdateView(APIView):
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_object(self):
    #     return self.request.user

    # def get_serializer_context(self):
    #     return {'request': self.request}

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     user_serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     user_serializer.is_valid(raise_exception=True)
    #     user_serializer.save()

    #     profile_serializer = ProfileSerializer(instance.profile, data=request.data.get('profile'), partial=partial)
    #     profile_serializer.is_valid(raise_exception=True)
    #     profile_serializer.save()

    #     return Response(user_serializer.data)
    
    # def get(self, request):
    #     serializer = self.serializer_class(self.get_object())
    #     return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user_serializer = UserSerializer(request.user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        profile_serializer = ProfileSerializer(request.user.profile, data=request.data.get('profile'), partial=True)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return Response(user_serializer.data)