from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from ..models import Achievement


@admin.register(Achievement)
class AchievementAdmin(BaseAdmin):
    """UI for Achievement model."""

    ordering = (
        "event",
    )
    list_display = (
        "user",
        "challenge",
        "event",
        "is_approved",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "user",
                    "challenge",
                    "event",
                ),
            },
        ),
        (
            _("Permissions"), {
                "fields": (
                    "is_approved",
                ),
            },
        ),
    )
