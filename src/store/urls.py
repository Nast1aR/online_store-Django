from django.urls import path

from store.views import *

urlpatterns = [
    path('colors/', ColorAPIView.as_view(), name='colors'),
    path('brands/', BrandAPIView.as_view(), name='brands'),
    path('materials/', MaterialAPIView.as_view(), name='materials'),
    path('product-main-on-sale/', ProductMainOnSaleAPIView.as_view(), name='product_main_on_sale'),
    path('product-main-new-arrives/', ProductMainNewArrivesAPIView.as_view(), name='product_main_new_arrives'),
]
