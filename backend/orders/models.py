from django.db import models
from django.conf import settings
from inventory.models import Product


class Customer(models.Model):
    name       = models.CharField(max_length=200)
    phone      = models.CharField(max_length=15, blank=True)
    email      = models.EmailField(blank=True)
    gstin      = models.CharField(max_length=15, blank=True)
    address    = models.TextField(blank=True)
    state_code = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SalesOrder(models.Model):
    STATUS_CHOICES = [
        ("draft",     "Draft"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    invoice_number = models.CharField(max_length=20, unique=True, blank=True)
    customer       = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    order_date     = models.DateField(auto_now_add=True)
    status         = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    subtotal       = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cgst_total     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sgst_total     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    igst_total     = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    grand_total    = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_interstate  = models.BooleanField(default=False)
    notes          = models.TextField(blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last = SalesOrder.objects.order_by("id").last()
            next_id = (last.id + 1) if last else 1
            self.invoice_number = f"INV-{next_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number


class OrderItem(models.Model):
    order       = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
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