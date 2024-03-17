from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Index
from uuid import uuid4

# Create your models here.


class Order(models.Model):
    order_id = models.UUIDField(default=uuid4, unique=True)
    customer_id = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.JSONField(encoder=DjangoJSONEncoder)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            Index(fields=["order_id"], name="order_id_idx"),
            Index(
                fields=["order_id", "customer_id", "-created_at"],
                name="order_customer_created_idx",
            ),
        ]
