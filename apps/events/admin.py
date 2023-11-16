from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from . import models


@admin.register(models.Event)
class EventAdmin(BaseAdmin):
    """UI for Event model."""

    ordering = (
        "title",
    )
    list_display = (
        "title",
        "is_public",
        "owner",
    )
    search_fields = (
        "title",
    )
    filter_horizontal = (
        "moderators",
        "members",
        "challenge_groups",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "title",
                ),
            },
        ),
        (
            _("General"), {
                "fields": (
                    "members",
                    "challenge_groups",
                ),
            },
        ),
        (
            _("Permissions"), {
                "fields": (
                    "is_public",
                    "owner",
                    "moderators",
                ),
            },
        ),
    )
