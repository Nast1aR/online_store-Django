from django.urls import path
from .api import UserCreateAPI, UserRetrieveAPI

urlpatterns = [
    path("create/", UserCreateAPI.as_view(), name="user-create"),
    path("retrieve/<int:pk>/", UserRetrieveAPI.as_view(), name="user-retrieve"),
]


