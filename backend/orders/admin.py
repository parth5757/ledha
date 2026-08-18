from django.contrib import admin
from .models import Customer, SalesOrder, OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "gstin", "created_at")
    search_fields = ("name", "phone", "gstin")


class OrderItemInline(admin.TabularInline):
    model  = OrderItem
    extra  = 1

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("invoice number", "customer", "grand_total", "status", "order_date")
    list_filter = ("status")
    search_fields = ("invoice_number", "customer_name")
    inlines = {OrderItemInline}