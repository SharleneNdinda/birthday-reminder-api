# Common models used within the project
from django.db import models

from birthday_reminder.common.models import AbstractBase


class Reminder(AbstractBase):
    """Holds information relating to reminders."""
    