from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


@receiver(post_save, sender="orders.SalesOrder")
def deduct_stock_on_order_confirm(sender, instance, **kwargs):
    if instance.status == "confirmed":
        from .models import StockMovement
        from orders.models import OrderItem
        with transaction.atomic():
            items = OrderItem.objects.filter(order=instance)
            for item in items:
                product = item.product
                product.current_stock -= item.quantity
                product.save()
                StockMovement.objects.get_or_create(
                    product        = product,
                    movement_type  = "OUT",
                    reference_type = "order",
                    reference_id   = instance.id,
                    defaults={
                        "quantity": item.quantity,
                        "note": f"Auto deducted for invoice {instance.invoice_number}",
                    }
                )


@receiver(post_save, sender="purchases.PurchaseOrder")
def add_stock_on_purchase_receive(sender, instance, **kwargs):
    if instance.status == "received":
        from .models import StockMovement
        from purchases.models import PurchaseItem
        with transaction.atomic():
            items = PurchaseItem.objects.filter(purchase=instance)
            for item in items:
                product = item.product
                product.current_stock += item.quantity
                product.save()
                StockMovement.objects.get_or_create(
                    product        = product,
                    movement_type  = "IN",
                    reference_type = "purchase",
                    reference_id   = instance.id,
                    defaults={
                        "quantity": item.quantity,
                        "note": f"Auto added for purchase {instance.bill_number}",
                    }
                )