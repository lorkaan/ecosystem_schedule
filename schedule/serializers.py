from rest_framework import serializers

from foundations.ecosystem_foundations.base.serializers import (
    ActiveSerializerMixin,
    TimeAuditableSerializerMixin,
    BaseItemTypeSerializerMixin,
    CreatedBySerializerMixin,
)
from .models import Deadline, DeadlineScheduleItemStatus, DeadlineScheduleItemType, Event, EventScheduleItemStatus, EventScheduleItemType

class BaseScheduleItemSerializerMixin(
    CreatedBySerializerMixin,
    ActiveSerializerMixin,
    TimeAuditableSerializerMixin,
    serializers.ModelSerializer
):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        abstract = True

class BaseScheduleItemTypeSerializerMixin(
    BaseItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    requires_title = serializers.BooleanField(
        required=False
    )

    default_title = serializers.CharField(
        required=False,
        allow_blank=True
    )

    requires_assignment = serializers.BooleanField(
        required=False
    )

    class Meta:
        abstract = True

class EventScheduleItemStatusSerializer(
    BaseItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = EventScheduleItemStatus
        fields = [
            "id",
            "name",
            "code",
        ]

class DeadlineScheduleItemStatusSerializer(
    BaseItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = DeadlineScheduleItemStatus
        fields = [
            "id",
            "name",
            "code",
        ]

class EventScheduleItemTypeSerializer(
    BaseScheduleItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = EventScheduleItemType
        fields = [
            "id",
            "name",
            "code",
            "requires_title",
            "default_title",
            "requires_assignment",
        ]

class DeadlineScheduleItemTypeSerializer(
    BaseScheduleItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = DeadlineScheduleItemType
        fields = [
            "id",
            "name",
            "code",
            "requires_title",
            "default_title",
            "requires_assignment",
        ]

class EventSerializer(
    BaseScheduleItemSerializerMixin,
    serializers.ModelSerializer
):
    type = serializers.PrimaryKeyRelatedField(
        queryset=EventScheduleItemType.objects.all()
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset=EventScheduleItemStatus.objects.all()
    )

    class Meta:
        model = Event
        fields = [
            "id",

            # base
            "title",
            "description",

            # scheduling
            "start_time",
            "end_time",

            # classification
            "type",
            "status",

            # lifecycle
            "is_active",
            "deactivated_at",

            # audit
            "created_at",
            "updated_at",
            "created_by",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        data = super().validate(data)

        start = data.get(
            "start_time",
            getattr(self.instance, "start_time", None)
        )

        end = data.get(
            "end_time",
            getattr(self.instance, "end_time", None)
        )

        if start and end and end <= start:
            raise serializers.ValidationError(
                "end_time must be after start_time"
            )

        return data

class DeadlineSerializer(
    BaseScheduleItemSerializerMixin,
    serializers.ModelSerializer
):
    type = serializers.PrimaryKeyRelatedField(
        queryset=DeadlineScheduleItemType.objects.all()
    )

    status = serializers.PrimaryKeyRelatedField(
        queryset=DeadlineScheduleItemStatus.objects.all()
    )

    class Meta:
        model = Deadline
        fields = [
            "id",

            # base
            "title",
            "description",

            # scheduling
            "due_time",

            # classification
            "type",
            "status",

            # lifecycle
            "is_active",
            "deactivated_at",

            # audit
            "created_at",
            "updated_at",
            "created_by",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]