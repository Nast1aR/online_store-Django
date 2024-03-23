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
    list_display = ['name', 'url']
    prepopulated_fields = {'url': ('name',)}


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    prepopulated_fields = {'url': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'get_image']
    prepopulated_fields = {'url': ('name',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} height=100>')


@admin.register(ProductType)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['url', 'type',]
    prepopulated_fields = {'url': ('type',)}
    list_display_links = ['type',]


class ImagesInline(admin.TabularInline):
    model = ProductInventoryImages


class AttributesInline(admin.TabularInline):
    model = ProductInventoryAttributes


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_type']
    prepopulated_fields = {'url': ('product_name',)}
    list_display_links = ['product_name',]


@admin.register(ProductInventory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product__name', 'get_image', 'quantity', 'priceUAH']
    readonly_fields = ['sale',]
    list_display_links = ['product__product_name',]
    form = ProductAdminForm
    inlines = [
        ImagesInline, AttributesInline,
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} height=100>')
