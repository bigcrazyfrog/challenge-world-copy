from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class ChallengeGroup(BaseModel):
    """Challenge group model."""

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=30,
    )
    is_public = models.BooleanField(
        verbose_name=_("Is public"),
        default=False,
    )
    owner = models.ForeignKey(
        to="users.User",
        related_name="challenge_groups",
        on_delete=models.PROTECT,
        verbose_name=_("Owner"),
        null=True,
    )
    challenges = models.ManyToManyField(
        to="challenges.Challenge",
        related_name="groups",
        related_query_name="group",
        verbose_name=_("Challenges"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Challenge group")
        verbose_name_plural = _("Challenge groups")

    def __repr__(self) -> str:
        return f"Challenge<{self.title}>"

    def __str__(self) -> str:
        return self.title
