from django.urls import path
from .api import UserCreateAPI, UserRetrieveAPI
from .views import  AddFavoriteProductTypesView, RemoveFavoriteProductTypesView, ListFavoriteProductTypessView
from .api import UserUpdateAPI

urlpatterns = [
    # path("create/", UserCreateAPI.as_view(), name="user-create"),
    path("retrieve/<int:id>/", UserRetrieveAPI.as_view(), name="user-retrieve"),
    path('update/<int:id>/', UserUpdateAPI.as_view(), name='user-update'), 
    path('favorites/add/', AddFavoriteProductTypesView.as_view(), name='add_favorite_product'),
    path('favorites/remove/<int:pk>/', RemoveFavoriteProductTypesView.as_view(), name='remove_favorite_product'),
    path('favorites/list/', ListFavoriteProductTypessView.as_view(), name='list_favorite_products'),
]


