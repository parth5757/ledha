from django.contrib import admin
from .models import Supplier, PurchaseOrder, PurchaseItem


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display  = ("name", "phone", "gstin")
    search_fields = ("name", "phone")


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display  = ("bill_number", "supplier", "grand_total", "status", "purchase_date")
    list_filter   = ("status",)
    search_fields = ("bill_number", "supplier__name")
    inlines       = [PurchaseItemInline]