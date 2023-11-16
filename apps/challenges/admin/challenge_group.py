from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .. import models


@admin.register(models.ChallengeGroup)
class ChallengeGroupAdmin(BaseAdmin):
    """UI for Challenge group model."""

    ordering = (
        "pk",
    )
    list_display = (
        "pk",
        "title",
        "owner",
        "is_public",
    )
    list_display_links = (
        "title",
    )
    search_fields = (
        "title",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "title",
                    "owner",
                ),
            },
        ),
        (
            _("Permissions"), {
                "fields": (
                    "is_public",
                ),
            },
        ),
        (
            _("Category"), {
                "fields": (
                    "challenges",
                ),
            },
        ),
    )
