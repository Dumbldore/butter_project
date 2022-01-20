from celery import shared_task
from django.db.models import Sum
from rest_framework.exceptions import ValidationError

from butter_app.models.activity import (Activity, ActivityAggregatedSerializer,
                                        ActivitySerializer, TaskStatus)


def get_aggregated_activity(track_id: str):
    last_status = (
        Activity.objects.filter(track_id=track_id).latest("activity_date").status
    )
    sums = (
        Activity.objects.filter(track_id=track_id, status=TaskStatus.S.value)
        .aggregate(Sum("billing_amount"))
        .get("billing_amount__sum", 0)
        or 0
    )
    reductions = (
        Activity.objects.filter(track_id=track_id, status=TaskStatus.R.value)
        .aggregate(Sum("billing_amount"))
        .get("billing_amount__sum", 0)
        or 0
    )
    billing_amount = round(sums - reductions, 2)
    data = {
        "track_id": track_id,
        "amount": billing_amount,
        "last_status": last_status,
    }
    serializer = ActivityAggregatedSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data


@shared_task()
def save_activities(activities):
    if type(activities) != list:
        activities = [activities]
    for activity in activities:
        try:
            ActivitySerializer(data=activity).is_valid(raise_exception=True)
        except ValidationError:
            activities.remove(activity)
    serializer = ActivitySerializer(data=activities, many=True)
    serializer.is_valid()
    serializer.save()
