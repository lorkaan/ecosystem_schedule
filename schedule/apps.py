from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'ecosystem_schedule.schedule'

    def ready(self):
        from .models import Event, Deadline
        from foundations.ecosystem_foundations.base.registry import NOTABLE_MODELS
        from foundations.ecosystem_foundations.users.registry import USER_ASSIGNABLE_MODELS_REGISTRY

        USER_ASSIGNABLE_MODELS_REGISTRY.add(Event, Deadline)
        NOTABLE_MODELS.add(Event, Deadline)
