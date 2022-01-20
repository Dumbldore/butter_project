from decimal import Decimal
from enum import Enum

from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers

from butter_app.utils.utils import get_choices_for_enum


class TaskStatus(Enum):
    S = "S"
    A = "A"
    R = "R"


class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    activity_date = models.DateTimeField()
    track_id = models.CharField(max_length=200)
    status = models.CharField(choices=get_choices_for_enum(TaskStatus), max_length=1)
    billing_amount = models.DecimalField(
        decimal_places=2, max_digits=99, validators=[MinValueValidator(Decimal("0.00"))]
    )

    class Meta:
        unique_together = (
            "id",
            "activity_date",
            "track_id",
            "status",
            "billing_amount",
        )


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class ActivityAggregatedSerializer(serializers.Serializer):
    track_id = serializers.CharField(required=True)
    last_status = serializers.ChoiceField(
        choices=get_choices_for_enum(TaskStatus), required=True
    )
    amount = serializers.DecimalField(decimal_places=2, required=True, max_digits=99)
