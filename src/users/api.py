from rest_framework import generics
from rest_framework.permissions import AllowAny
from  .serializers import UserSerializer
from . models import User
from rest_framework.permissions import IsAuthenticated

class UserCreateAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserUpdateAPI(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
