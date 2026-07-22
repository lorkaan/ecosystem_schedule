from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'schedule'

    def ready(self):
        from .models import Event, Deadline
        from ecosystem_foundations.base.registry import ASSIGNABLE_MODELS, NOTABLE_MODELS

        ASSIGNABLE_MODELS.add(Event, Deadline)
        NOTABLE_MODELS.add(Event, Deadline)
