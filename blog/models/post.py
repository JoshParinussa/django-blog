"""Banner models."""
from django.db import models
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField

from blog.helpers import file as file_helper
from .base import BaseModel


class Post(BaseModel):
    """Blog model."""

    title = models.CharField(_("title"), max_length=255, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name=('blog'), verbose_name=_('category'))
    content = models.TextField(_("content"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField(_("image"), upload_to=file_helper.DateUploadPath('blog/blog'))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
