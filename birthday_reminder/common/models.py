"""Common models used across the project."""
import uuid

from django.db import models


class AbstractBase(models.Model):
    """Base abstract model."""

    guid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(editable=False) 
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.UUIDField()

    class Meta:
        """Define a sensible default ordering."""

        abstract = True
