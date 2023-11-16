from enum import StrEnum

import django_filters

from .models import Event
from .queryset import EventQuerySet


class UserRole(StrEnum):
    """Enumeration of User roles in event."""

    OWNER = "owner"
    MODERATOR = "moderator"
    MEMBER = "member"


FILTER_CHOICES = (
    (UserRole.OWNER, UserRole.OWNER.title()),
    (UserRole.MODERATOR, UserRole.MODERATOR.title()),
    (UserRole.MEMBER, UserRole.MEMBER.title()),
)


class EventFilter(django_filters.FilterSet):
    """FilterSet for Events."""

    role = django_filters.ChoiceFilter(
        method="_role_filter",
        label="Select user role",
        choices=FILTER_CHOICES,
    )

    # pylint: disable=unused-argument
    def _role_filter(
        self,
        queryset: EventQuerySet,
        name: str,
        value: UserRole,
    ) -> EventQuerySet:
        """Filter by User role in event."""
        if self.user.is_anonymous:
            return queryset

        if value == UserRole.OWNER:
            return queryset.filter(owner=self.user)
        if value == UserRole.MODERATOR:
            return queryset.filter(moderators=self.user)
        if value == UserRole.MEMBER:
            return queryset.filter(members=self.user)
        return queryset

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix)
        self.user = request.user

    class Meta:
        model = Event
        fields = (
            "is_public",
            "is_active",
        )
