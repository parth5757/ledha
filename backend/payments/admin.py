from django.contrib import admin
from .models import Payment, Borrow, BankStatement

@admin.site.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_type", "amount", "method", "payment_date", "order", "purchase")
    list_filter = ("payment_type", "method")
    search_fields = ("refrence_number", "note")


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display  = ("party_name", "borrow_type", "amount", "borrow_date", "due_date", "is_settled")
    list_filter   = ("borrow_type", "is_settled")
    search_fields = ("party_name",)


@admin.register(BankStatement)
class BankStatementAdmin(admin.ModelAdmin):
    list_display  = ("entry_date", "description", "debit", "credit", "balance", "bank_name")
    search_fields = ("description",)