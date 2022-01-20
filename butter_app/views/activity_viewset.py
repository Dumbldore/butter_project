from django.db.models import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from butter_app.logic.activity_logic import (get_aggregated_activity,
                                             save_activities)
from butter_app.models.activity import Activity, ActivitySerializer


class ActivityViewSet(GenericViewSet, generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"

    def create(self, request):
        save_activities.apply_async(args=[request.data])
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def aggregated_information(self, request):
        try:
            track_id = request.query_params["track_id"]
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            response = get_aggregated_activity(track_id=track_id)
        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND, data="No object with given track_id"
            )
        return Response(response)
