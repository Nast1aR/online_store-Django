from django.urls import path

from store.views import *

urlpatterns = [
    path('colors/', ColorAPIView.as_view(), name='colors'),
    path('brands/', BrandAPIView.as_view(), name='brands'),
    path('materials/', MaterialAPIView.as_view(), name='materials'),
    path('product-main-list/', ProductListAPIView.as_view(), name='product_main_list'),
    path('product-new-arrives/', ProductNewArrivesAPIView.as_view(), name='product_new_arrives'),
]
