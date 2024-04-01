from django.urls import path
from .api import UserCreateAPI, UserRetrieveAPI
from .views import FavoriteProductsAPIView

urlpatterns = [
    path("create/", UserCreateAPI.as_view(), name="user-create"),
    path("retrieve/<int:pk>/", UserRetrieveAPI.as_view(), name="user-retrieve"),
    path('favorite-products/', FavoriteProductsAPIView.as_view(), name='favorite_products'),
]


