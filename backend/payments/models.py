from django.db import models
from django.conf import settings


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ("received", "Received"),
        ("paid",     "Paid"),
    ]
    METHOD_CHOICES = [
        ("cash",         "Cash"),
        ("upi",          "UPI"),
        ("bank_transfer","Bank Transfer"),
        ("cheque",       "Cheque"),
    ]

    order        = models.ForeignKey("orders.SalesOrder",    on_delete=models.PROTECT, null=True, blank=True, related_name="payments")
    purchase     = models.ForeignKey("purchases.PurchaseOrder", on_delete=models.PROTECT, null=True, blank=True, related_name="payments")
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    amount       = models.DecimalField(max_digits=12, decimal_places=2)
    method       = models.CharField(max_length=15, choices=METHOD_CHOICES, default="cash")
    reference_number = models.CharField(max_length=100, blank=True)
    payment_date = models.DateField()
    note         = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_type} ₹{self.amount} on {self.payment_date}"


class Borrow(models.Model):
    BORROW_TYPE_CHOICES = [
        ("given", "Given"),
        ("taken", "Taken"),
    ]

    borrow_type  = models.CharField(max_length=10, choices=BORROW_TYPE_CHOICES)
    party_name   = models.CharField(max_length=200)
    amount       = models.DecimalField(max_digits=12, decimal_places=2)
    borrow_date  = models.DateField()
    due_date     = models.DateField(null=True, blank=True)
    is_settled   = models.BooleanField(default=False)
    settled_date = models.DateField(null=True, blank=True)
    note         = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.borrow_type} ₹{self.amount} — {self.party_name}"


class BankStatement(models.Model):
    entry_date  = models.DateField()
    description = models.CharField(max_length=300)
    debit       = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit      = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bank_name   = models.CharField(max_length=100, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entry_date} — {self.description}"