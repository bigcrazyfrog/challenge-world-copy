from typing import Self

from django.db import models
from django.db.models import Q

from apps.users.models import User


class EventQuerySet(models.QuerySet):
    """Queryset class for `Event` model."""

    def available_for_user(self, user: User) -> Self:
        """Filter available `Event` instances for provided user."""
        if user.is_staff or user.is_superuser:
            return self

        return self.filter(
            Q(is_public=True)
            | Q(owner=user)
            | Q(moderators=user)
            | Q(members=user),
        )
