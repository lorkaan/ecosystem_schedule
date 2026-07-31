from django.contrib import admin

from .models import Deadline, DeadlineScheduleItemStatus, DeadlineScheduleItemType, Event, EventScheduleItemStatus, EventScheduleItemType

# Register your models here.
admin.register(EventScheduleItemStatus)
admin.register(DeadlineScheduleItemStatus)
admin.register(EventScheduleItemType)
admin.register(DeadlineScheduleItemType)
admin.register(Event)
admin.register(Deadline)