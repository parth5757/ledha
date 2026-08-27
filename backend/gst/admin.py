from django.contrib import admin
from .models import GSTEntry

@admin.register(GSTEntry)
class GSTEntryAdmin(admin.ModelAdmin):
    list_display = ("entry_type", "period_month", "taxable_value", "cgst", "sgst", "igst", "transaction_date")
    list_filter = ("entry_type", "period_month")