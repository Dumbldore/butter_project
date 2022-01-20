import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from butter_app.logic.activity_logic import save_activities
from butter_app.models.activity import Activity
from butter_app.tests.test_activity_viewset_mocks import (
    aggregate_activity, aggregate_activity_result, correct_activity,
    negative_price_task_activity, wrong_date_activity, wrong_status_activity)


class TestAnalyticsTaskViewSet(APITestCase):
    def setUp(self):
        self.url = reverse("ActivityViewSet-list")
        self.aggregate_url = reverse("ActivityViewSet-aggregated-information")

    def test_activity_viewset_returns_200_when_activity_created(self):
        response = self.client.post(
            self.url, data=json.dumps(correct_activity), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_viewset_dont_create_when_negative_price_activity_created(self):
        save_activities(activities=negative_price_task_activity.copy())

        activities = Activity.objects.filter(id=negative_price_task_activity[0]["id"])
        self.assertEqual(len(activities), 0)

    def test_activity_viewset_dont_create_when_wrong_status_activity_created(self):
        save_activities(activities=wrong_status_activity.copy())
        activities = Activity.objects.filter(id=wrong_status_activity[0]["id"])
        self.assertEqual(len(activities), 0)

    def test_activity_viewset_dont_create_when_wrong_date_activity_created(self):
        save_activities(activities=wrong_date_activity.copy())

        activities = Activity.objects.filter(id=wrong_date_activity[0]["id"])
        self.assertEqual(len(activities), 0)

    def test_activities_dont_create_duplicate(self):
        save_activities(activities=correct_activity.copy())
        save_activities(activities=correct_activity.copy())
        activities = Activity.objects.filter(id=correct_activity[0]["id"])
        self.assertEqual(len(activities), 1)

    def test_activity_viewset_properly_creates_activity(self):
        save_activities(activities=correct_activity.copy())
        activities1 = Activity.objects.filter(id=correct_activity[0]["id"])
        activities2 = Activity.objects.filter(id=correct_activity[1]["id"])
        self.assertEqual(len(activities1), 1)
        self.assertEqual(len(activities2), 1)

    def test_aggregated_information_returns_400_with_bad_request(self):
        self.client.post(
            self.url,
            data=json.dumps(aggregate_activity),
            content_type="application/json",
        )
        response = self.client.get(self.aggregate_url, {"xdd": "T1234567"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_aggregated_information_returns_404_for_non_existing_tracking_id(self):
        save_activities(activities=aggregate_activity)
        response = self.client.get(self.aggregate_url, {"track_id": "xddd"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_aggregated_information_returns_correct_output(self):
        save_activities(activities=aggregate_activity)
        result = self.client.get(self.aggregate_url, {"track_id": "T1234567"})
        self.assertEqual(result.data["track_id"], aggregate_activity_result["track_id"])
        self.assertEqual(
            result.data["last_status"], aggregate_activity_result["last_status"]
        )
        self.assertAlmostEqual(
            result.data["amount"], aggregate_activity_result["amount"], 2
        )
