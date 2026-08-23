from django.contrib import admin
from .models import Employee, Attendance, SalaryPayment


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display  = ("name", "phone", "role", "salary", "join_date", "is_active")
    search_fields = ("name", "phone")
    list_filter   = ("is_active",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display  = ("employee", "date", "status")
    list_filter   = ("status",)


@admin.register(SalaryPayment)
class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ("employee", "month", "amount_paid", "method", "payment_date")