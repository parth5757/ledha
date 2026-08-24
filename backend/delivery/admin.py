from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DelivertAdmin(admin.ModelAdmin):
    list_display = ("order", "employee", "status", "scheduled_date", "delivered_date")
    list_filter = ("status", )