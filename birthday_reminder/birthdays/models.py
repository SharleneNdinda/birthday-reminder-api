"""Birthday app related models."""
from django.db import models

from birthday_reminder.common.models import AbstractBase


class Birthday(AbstractBase):
    """Holds information about birthdays."""

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.title
