from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Achievement(BaseModel):
    """Challenge achievement model.

    Provide fixing the execution of the challenges.

    """

    user = models.ForeignKey(
        to="users.User",
        verbose_name=_("User"),
        related_name="achievements",
        on_delete=models.PROTECT,
    )
    challenge = models.ForeignKey(
        to="challenges.Challenge",
        verbose_name=_("Challenge"),
        related_name="achievements",
        on_delete=models.PROTECT,
    )
    event = models.ForeignKey(
        to="events.Event",
        verbose_name=_("Event"),
        related_name="achievements",
        on_delete=models.PROTECT,
    )
    is_approved = models.BooleanField(
        verbose_name=_("Is approved"),
        default=False,
        help_text=_("Is approved by moderator"),
    )

    class Meta:
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")
        unique_together = ("user", "challenge", "event")

    def __repr__(self) -> str:
        return f"Achievement<{self.challenge}>"

    def __str__(self) -> str:
        return (
            f"{self.user} completed {self.challenge} in {self.event}"
        )
