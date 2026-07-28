from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.


from ecosystem_foundations.base.views import (
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    TimeAuditableQuerysetMixin,
)

from .models import (
    Deadline,
    DeadlineScheduleItemStatus,
    DeadlineScheduleItemType,
    Event,
    EventScheduleItemStatus,
    EventScheduleItemType,
)

from .serializers import (
    DeadlineScheduleItemStatusSerializer,
    DeadlineScheduleItemTypeSerializer,
    DeadlineSerializer,
    EventScheduleItemStatusSerializer,
    EventScheduleItemTypeSerializer,
    EventSerializer,
)


# -------------------------------------------------
# Event Status
# -------------------------------------------------

class EventScheduleItemStatusViewSet(
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = EventScheduleItemStatus.objects.all()
    serializer_class = EventScheduleItemStatusSerializer


# -------------------------------------------------
# Deadline Status
# -------------------------------------------------

class DeadlineScheduleItemStatusViewSet(
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = DeadlineScheduleItemStatus.objects.all()
    serializer_class = DeadlineScheduleItemStatusSerializer


# -------------------------------------------------
# Event Types
# -------------------------------------------------

class EventScheduleItemTypeViewSet(
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = EventScheduleItemType.objects.all()
    serializer_class = EventScheduleItemTypeSerializer


# -------------------------------------------------
# Deadline Types
# -------------------------------------------------

class DeadlineScheduleItemTypeViewSet(
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = DeadlineScheduleItemType.objects.all()
    serializer_class = DeadlineScheduleItemTypeSerializer


# -------------------------------------------------
# Events
# -------------------------------------------------

class EventViewSet(
    ActiveQuerysetMixin,
    TimeAuditableQuerysetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = Event.objects.select_related(
        "type",
        "status",
        "created_by",
    )

    serializer_class = EventSerializer


# -------------------------------------------------
# Deadlines
# -------------------------------------------------

class DeadlineViewSet(
    ActiveQuerysetMixin,
    TimeAuditableQuerysetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = Deadline.objects.select_related(
        "type",
        "status",
        "created_by",
    )

    serializer_class = DeadlineSerializer