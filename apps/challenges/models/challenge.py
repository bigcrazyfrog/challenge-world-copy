from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Challenge(BaseModel):
    """Challenge model."""

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=30,
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )
    prize = models.TextField(
        verbose_name=_("Prize"),
        blank=True,
    )
    is_conveyable = models.BooleanField(
        verbose_name=_("Is conveyable"),
        default=False,
        help_text=_(
            "Can challenge be conveyed.",
        ),
    )
    author = models.ForeignKey(
        to="users.User",
        related_name="challenges",
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )
    tags = models.ManyToManyField(
        to="challenges.Tag",
        related_name="challenges",
        verbose_name=_("Tags"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Challenge")
        verbose_name_plural = _("Challenges")

    def __repr__(self) -> str:
        return f"Challenge<{self.title}>"

    def __str__(self) -> str:
        return self.title
