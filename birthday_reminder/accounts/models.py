from django.contrib.auth.models import AbstractUser
from django.db import models

from birthday_reminder.common.models import AbstractBase
    

class UserProfile(AbstractBase):
    """User's profile."""
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(blank=True)

class AuthUser(AbstractUser):
    """Custom Auth User model."""

    profile = models.ForeignKey(
        UserProfile, related_name="profile", on_delete=models.PROTECT
    )
