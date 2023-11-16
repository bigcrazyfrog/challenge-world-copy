from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChallengesConfig(AppConfig):
    """Default configuration for Challenges app."""

    name = "apps.challenges"
    verbose_name = _("Challenges")
