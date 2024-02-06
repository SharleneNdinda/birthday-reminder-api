# Common models used within the project
from django.db import models

from birthday_reminder.common.models import AbstractBase


class Birthday(AbstractBase):
    """Holds information about birthdays."""

    description = models.TextField(max_length=250)
    day = models.DateField()
