from django.db import models
from django.conf import settings


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Expense Categories"

    def __str__(self):
        return self.name


class Expense(models.Model):
    METHOD_CHOICES = [
        ("cash", "Cash"),
        ("upi",  "UPI"),
        ("bank", "Bank"),
    ]

    category     = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title        = models.CharField(max_length=200)
    amount       = models.DecimalField(max_digits=12, decimal_places=2)
    expense_date = models.DateField()
    method       = models.CharField(max_length=10, choices=METHOD_CHOICES, default="cash")
    note         = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ₹{self.amount}"