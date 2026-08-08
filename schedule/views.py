from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


from foundations.ecosystem_foundations.base.views import (
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    TimeAuditableQuerysetMixin,
    FilterSchemaMixin
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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",   # from your mixin
        "code",
    ]

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "name",
        "code",
    ]

    ordering = ["name"]


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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",
        "code",
    ]

    search_fields = [
        "name",
        "code",
    ]

    ordering_fields = [
        "name",
        "code",
    ]

    ordering = ["name"]


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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",
        "code",
        "requires_title",
        "requires_assignment",
    ]

    search_fields = [
        "name",
        "code",
        "default_title",
    ]

    ordering_fields = [
        "name",
        "code",
        "default_title",
    ]

    ordering = ["name"]

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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",
        "code",
        "requires_title",
        "requires_assignment",
    ]

    search_fields = [
        "name",
        "code",
        "default_title",
    ]

    ordering_fields = [
        "name",
        "code",
        "default_title",
    ]

    ordering = ["name"]

# -------------------------------------------------
# Events
# -------------------------------------------------

class EventViewSet(
    ActiveQuerysetMixin,
    TimeAuditableQuerysetMixin,
    BaseQueryViewSetMixin,
    FilterSchemaMixin,
    viewsets.ModelViewSet,
):
    queryset = Event.objects.select_related(
        "type",
        "status",
        "created_by",
    )

    serializer_class = EventSerializer

    # 🔽 Add these
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Exact filtering
    filterset_fields = {
        "type": ["exact"],
        "status": ["exact"],
        "is_active": ["exact"],
        "created_by": ["exact"],
        "start_time": ["gte", "lte"],
        "end_time": ["gte", "lte"]
    }

    # Text search
    search_fields = [
        "title",
        "description",
    ]

    # Sorting
    ordering_fields = [
        "start_time",
        "end_time",
        "created_at",
        "updated_at",
        "title",
    ]

    # Default ordering
    ordering = ["start_time"]


# -------------------------------------------------
# Deadlines
# -------------------------------------------------

class DeadlineViewSet(
    ActiveQuerysetMixin,
    TimeAuditableQuerysetMixin,
    BaseQueryViewSetMixin,
    FilterSchemaMixin,
    viewsets.ModelViewSet,
):
    queryset = Deadline.objects.select_related(
        "type",
        "status",
        "created_by",
    )

    serializer_class = DeadlineSerializer

    # 🔽 Filtering setup
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Exact + range filtering
    filterset_fields = {
        "type": ["exact"],
        "status": ["exact"],
        "is_active": ["exact"],
        "created_by": ["exact"],
        "due_time": ["exact", "gte", "lte"],
    }

    # Text search
    search_fields = [
        "title",
        "description",
    ]

    # Ordering
    ordering_fields = [
        "due_time",
        "created_at",
        "updated_at",
        "title",
    ]

    ordering = ["due_time"]