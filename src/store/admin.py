from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from django import forms
from store.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color', 'color_id']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material', 'material_id']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand', 'brand_id', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} height=100>')


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['main_category_id', 'main_category',]
    list_display_links = ['main_category',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category',]
    list_display_links = ['category',]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['cat', 'sub_category', 'subcategory_id',]
    list_display_links = ['sub_category',]


class ImagesInline(admin.TabularInline):
    model = ProductImages


class AttributesInline(admin.TabularInline):
    model = ProductAttributes


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'get_image', 'quantity', 'total_quantity', 'product_type', 'priceUAH']
    readonly_fields = ['sale',]
    list_display_links = ['product_name',]
    form = ProductAdminForm
    inlines = [
        ImagesInline, AttributesInline,
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} height=100>')
