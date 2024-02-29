from django.contrib.auth.models import AbstractUser
from django.db import models

from birthday_reminder.common.models import AbstractBase


class UserProfile(AbstractBase):
    """User's profile."""

    bio = models.TextField(max_length=255)
    gender = models.CharField(null=True, blank=True)
    date_of_birth = models.DateField()


class AuthUser(AbstractUser):
    """Custom Auth User model."""

    profile = models.OneToOneField(
        UserProfile, related_name="user", on_delete=models.PROTECT
    )
