"""Base model."""
import uuid

from django.db import models


class BaseModel(models.Model):
    """BaseModel class."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:  # noqa: D106
        abstract = True
