from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Tag(BaseModel):
    """Challenge tag model."""

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __repr__(self) -> str:
        return f"Tag<{self.name}>"

    def __str__(self) -> str:
        return self.name
