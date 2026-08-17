from django.contrib import admin
from .models import Category, Product, StockMovment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "crated_at")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ("name", "category", "selling_price", "current_stock", "unit", "is_active")
    search_fields = ("name", "sku", "hsn_code")
    list_filter   = ("category", "is_active", "gst_rate")


@admin.register(StockMovment)
class StockMovmentAdmin(admin.ModelAdmin):
    list_display = ("product", "movement_type", "Inventory", "refrence_type", "created_at")
    list_filter = ("movement_type", "refrence_type")