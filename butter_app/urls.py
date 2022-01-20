from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers

from butter_app.views.activity_viewset import ActivityViewSet

router = routers.DefaultRouter()
router.register(r"activity", ActivityViewSet, basename="ActivityViewSet")

urlpatterns = [
    path("admin/", admin.site.urls),
    url("api/", include(router.urls)),
    path("", RedirectView.as_view(url=f"/{settings.HOME_URL}/")),
]
