from django.urls import path

from store.views import *

urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view(), name='categories'),
    path('accessories/', AccessoriesListAPIView.as_view(), name='accessories'),
    path('brands/', BrandAPIView.as_view(), name='brands'),
    path('colors/', ColorAPIView.as_view(), name='colors'),
    path('materials/', MaterialAPIView.as_view(), name='materials'),
    path('product-main-on-sale/', ProductMainOnSaleAPIView.as_view(), name='product_main_on_sale'),
    path('product-main-new-arrives/', ProductMainNewArrivesAPIView.as_view(), name='product_main_new_arrives'),
    path('product-detail/', Product)
]
