"""Birthday Views."""
from rest_framework import viewsets

from birthday_reminder.birthdays.models import Birthday


class BirthdayViewSet(viewsets.ModelViewSet):
    """Birthday ViewSet.

    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Birthday.objects.all()
