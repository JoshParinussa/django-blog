"""Banner models."""
from django.db import models
from django.utils.translation import gettext as _

from .base import BaseModel


class Category(BaseModel):
    """Category model."""

    title = models.CharField(_("title"), max_length=255, db_index=True)

    def __str__(self):
        return self.title
