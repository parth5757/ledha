from django.db import models


class Delivery(models.Model):
    STATUS_CHOICES = [
        ("pending",    "Pending"),
        ("dispatched", "Dispatched"),
        ("delivered",  "Delivered"),
        ("failed",     "Failed"),
    ]

    order            = models.OneToOneField("orders.SalesOrder", on_delete=models.PROTECT, related_name="delivery")
    employee         = models.ForeignKey("employees.Employee", on_delete=models.SET_NULL, null=True, blank=True)
    delivery_address = models.TextField()
    status           = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")
    scheduled_date   = models.DateField(null=True, blank=True)
    delivered_date   = models.DateField(null=True, blank=True)
    note             = models.TextField(blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery for {self.order.invoice_number} — {self.status}"