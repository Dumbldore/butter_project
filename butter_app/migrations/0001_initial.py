# Generated by Django 3.2.11 on 2022-01-20 03:37

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("activity_date", models.DateTimeField()),
                ("track_id", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[("S", "S"), ("A", "A"), ("R", "R")], max_length=1
                    ),
                ),
                (
                    "billing_amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=99,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.00"))
                        ],
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("id", "activity_date", "track_id", "status", "billing_amount")
                },
            },
        ),
    ]
