from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_url = "Categories"


    def __str__(self):
        return self.name



class Product(models.Model):
    UNIT_CHOICES = [
        ("pcs", "pieces"),
        ("kg", "Kilograms"),
        ("liter", "Liter"),
        ("meter", "Meter"),
        ("box", "Box"),
        ("packet", "Packets")
    ]

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    sku = models.CharField(maxx_length=50, unique=True, blank=True)
    hsn_code = models.CharField(max_length=8, blank=True)
    gst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_stock_level = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default="pcs")
    is_active = models.BooleanField(default=True)
    created_at = models.DecimalField(default=True)

    def __str__(self):
        return self.name


class StockMovment(models.Model):
    MOVEMENT_CHOICES = [
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
        ("ADJUST", "Adjustment"), 
    ]

    REF_CHOICES = [
        ("order", "Sales Order"),
        ("purchase", "Purchase"), 
        ("manual", "Manual"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="movements")
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    reference_type = models.CharField(max_length=10, choices=REF_CHOICES, default="mmanual")
    reference_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type}, {self.quantity} - {self.product.name}"


    