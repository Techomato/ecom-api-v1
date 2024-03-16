# from django.contrib import admin
from django.contrib import admin

from products.models.db_models.category import Category
from products.models.db_models.product import Product
from products.models.db_models.sub_category import SubCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "updated_at")
    list_filter = ("seller_id",)
    ordering = ["updated_at"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "updated_at")
    ordering = ["updated_at"]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "updated_at")
    ordering = ["updated_at"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

admin.site.site_header = "Shoppixa Administration"
admin.site.site_title = "Shoppixa Administration"
admin.site.index_title = "Shoppixa"
admin.empty_value_display = "**Empty**"
