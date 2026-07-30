from django.db import models
from django.core.exceptions import ValidationError
import pghistory

from foundations.ecosystem_foundations.base.models import BaseUuidPrimaryKeyModel, TimeAuditableMixin, ActiveMixin, BaseItemType, CreatedByMixin
# Create your models here.

class ScheduleStatus(models.TextChoices):
    SCHEDULED = 'S', "Scheduled"
    ACTIVE = 'A', "Active"
    FINISHED = 'F', "Completed"
    CANCELLED = 'C', "Cancelled"
    MISSED = 'M', "Missed"

class BaseScheduleItemStatus(BaseItemType):

    class Meta:
        abstract = True

class EventScheduleItemStatus(BaseScheduleItemStatus):
    pass

class DeadlineScheduleItemStatus(BaseScheduleItemStatus):
    pass

class BaseScheduleItemType(BaseItemType):
    requires_title = models.BooleanField(default=True)
    default_title = models.CharField(max_length=255, blank=True)

    requires_assignment = models.BooleanField(default=False)

    class Meta:
        abstract = True

class EventScheduleItemType(BaseScheduleItemType):
    pass

class DeadlineScheduleItemType(BaseScheduleItemType):
    pass

# Create your models here.
class BaseScheduleItem(CreatedByMixin, ActiveMixin, TimeAuditableMixin, BaseUuidPrimaryKeyModel):

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        abstract = True

@pghistory.track()
class Event(BaseScheduleItem):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    type = models.ForeignKey(
        EventScheduleItemType,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items"
    )

    status = models.ForeignKey(
        EventScheduleItemStatus,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_events"
    )

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("end_time must be after start_time")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


@pghistory.track()
class Deadline(BaseScheduleItem):
    due_time = models.DateTimeField()

    type = models.ForeignKey(
        DeadlineScheduleItemType,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_items"
    )

    status = models.ForeignKey(
        DeadlineScheduleItemStatus,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_deadlines"
    )