from django.urls import path

from store.views import *

urlpatterns = [
    path('main-categories/', MainCategoryAPIView.as_view(), name='main_categories'),
    path('main-category-product-list/<slug:main_category_url>/', ProductMainCategoryListAPIView.as_view(), name='main_categories_product_list'),
    path('brands/', BrandAPIView.as_view(), name='brands'),
    path('colors/', ColorAPIView.as_view(), name='colors'),
    path('materials/', MaterialAPIView.as_view(), name='materials'),
    path('product-main-on-sale/', ProductMainOnSaleAPIView.as_view(), name='product_main_on_sale'),
    path('product-main-new-arrives/', ProductMainNewArrivesAPIView.as_view(), name='product_main_new_arrives'),
]
