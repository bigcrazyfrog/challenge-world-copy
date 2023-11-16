from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel

from .queryset import EventQuerySet


class Event(BaseModel):
    """Event model."""

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=30,
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active"),
        default=True,
    )
    is_public = models.BooleanField(
        verbose_name=_("Is public"),
        default=False,
    )
    owner = models.ForeignKey(
        to="users.User",
        on_delete=models.PROTECT,
        related_name="owned_events",
        verbose_name=_("Owner"),
    )
    moderators = models.ManyToManyField(
        to="users.User",
        related_name="moderated_events",
        verbose_name=_("Moderators"),
        blank=True,
    )
    members = models.ManyToManyField(
        to="users.User",
        related_name="available_events",
        verbose_name=_("Members"),
        blank=True,
    )
    challenge_groups = models.ManyToManyField(
        to="challenges.ChallengeGroup",
        related_name="events",
        verbose_name=_("Challenge groups"),
        blank=True,
    )

    objects = EventQuerySet.as_manager()

    def __repr__(self) -> str:
        return f"Event<{self.title}>"

    def __str__(self) -> str:
        return self.title
