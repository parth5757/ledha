from django.db import models
from django.conf import settings
from inventory.models import Product


class Supplier(models.Model):
    name       = models.CharField(max_length=200)
    phone      = models.CharField(max_length=15, blank=True)
    gstin      = models.CharField(max_length=15, blank=True)
    address    = models.TextField(blank=True)
    state_code = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ("pending",   "Pending"),
        ("received",  "Received"),
        ("cancelled", "Cancelled"),
    ]

    bill_number  = models.CharField(max_length=50, unique=True)
    supplier     = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    created_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    purchase_date= models.DateField()
    status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    subtotal     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cgst_total   = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sgst_total   = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    igst_total   = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    grand_total  = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes        = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bill_number


class PurchaseItem(models.Model):
    purchase    = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="items")
    product     = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity    = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)
    gst_rate    = models.DecimalField(max_digits=5,  decimal_places=2)
    cgst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sgst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    igst_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    line_total  = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"