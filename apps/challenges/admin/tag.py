from django.contrib import admin

from apps.core.admin import BaseAdmin

from .. import models


class ChallengeInline(admin.TabularInline):
    """Inline mode for Challenge model."""

    model = models.Challenge.tags.through

    verbose_name = "Challenge"
    verbose_name_plural = "Challenges"

    extra = 0
    max_num = 100


@admin.register(models.Tag)
class TagAdmin(BaseAdmin):
    """UI for Tag model."""

    ordering = (
        "name",
    )
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )
    inlines = (
        ChallengeInline,
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "name",
                ),
            },
        ),
    )
