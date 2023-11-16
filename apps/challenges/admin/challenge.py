from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .. import models


class ChallengeGroupInline(admin.TabularInline):
    """Inline mode for challenge model."""

    model = models.ChallengeGroup.challenges.through

    verbose_name = _("Group")
    verbose_name_plural = _("Groups")

    extra = 0
    max_num = 100


@admin.register(models.Challenge)
class ChallengeAdmin(BaseAdmin):
    """UI for Challenge model."""

    ordering = (
        "title",
    )
    list_display = (
        "title",
        "description",
        "prize",
        "is_conveyable",
        "author",
    )
    search_fields = (
        "title",
        "description",
    )
    filter_horizontal = (
        "tags",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "title",
                    "description",
                ),
            },
        ),
        (
            _("Prize"), {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "prize",
                ),
            },
        ),
        (
            _("Permissions"), {
                "fields": (
                    "is_conveyable",
                    "author",
                ),
            },
        ),
        (
            _("Category"), {
                "fields": (
                    "tags",
                ),
            },
        ),
    )
