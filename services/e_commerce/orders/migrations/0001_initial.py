# Generated by Django 5.0.3 on 2024-03-17 10:05

import django.core.serializers.json
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("customer_id", models.CharField(max_length=100)),
                ("order_status", models.CharField(max_length=100)),
                ("order_total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order_items",
                    models.JSONField(
                        encoder=django.core.serializers.json.DjangoJSONEncoder
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "indexes": [
                    models.Index(fields=["order_id"], name="order_id_idx"),
                    models.Index(
                        fields=["order_id", "customer_id", "-created_at"],
                        name="order_customer_created_idx",
                    ),
                ],
            },
        ),
    ]
