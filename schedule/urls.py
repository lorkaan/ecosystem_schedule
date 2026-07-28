from rest_framework.routers import DefaultRouter

from .views import (
    DeadlineScheduleItemStatusViewSet,
    DeadlineScheduleItemTypeViewSet,
    DeadlineViewSet,
    EventScheduleItemStatusViewSet,
    EventScheduleItemTypeViewSet,
    EventViewSet,
)


router = DefaultRouter()

# Primary resources
router.register(
    r"events",
    EventViewSet,
    basename="event"
)

router.register(
    r"deadlines",
    DeadlineViewSet,
    basename="deadline"
)


# Event configuration
router.register(
    r"event-types",
    EventScheduleItemTypeViewSet,
    basename="event-type"
)

router.register(
    r"event-statuses",
    EventScheduleItemStatusViewSet,
    basename="event-status"
)


# Deadline configuration
router.register(
    r"deadline-types",
    DeadlineScheduleItemTypeViewSet,
    basename="deadline-type"
)

router.register(
    r"deadline-statuses",
    DeadlineScheduleItemStatusViewSet,
    basename="deadline-status"
)


urlpatterns = router.urls