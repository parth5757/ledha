from django.db import models


class GSTEntry(models.Model):
    ENTRY_TYPE_CHOICES = [
        ("sale",     "Sale"),
        ("purchase", "Purchase"),
    ]

    order         = models.ForeignKey("orders.SalesOrder",      on_delete=models.CASCADE, null=True, blank=True, related_name="gst_entries")
    purchase      = models.ForeignKey("purchases.PurchaseOrder", on_delete=models.CASCADE, null=True, blank=True, related_name="gst_entries")
    entry_type    = models.CharField(max_length=10, choices=ENTRY_TYPE_CHOICES)
    gstin_party   = models.CharField(max_length=15, blank=True)
    hsn_code      = models.CharField(max_length=8,  blank=True)
    taxable_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cgst          = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sgst          = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    igst          = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    place_of_supply  = models.CharField(max_length=2, blank=True)
    period_month     = models.CharField(max_length=7)   # format: 2025-06
    transaction_date = models.DateField()
    created_at       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "GST Entries"

    def __str__(self):
        return f"{self.entry_type} — {self.period_month} — ₹{self.taxable_value}"