"""Birthdays URLs."""
from rest_framework.routers import SimpleRouter

from birthday_reminder.birthdays import views


router = SimpleRouter()
router.register("birthdays", views.BirthdayViewSet)

urlpatterns = router.urls
