import django_filters

from .models import Challenge


class ChallengeFilter(django_filters.FilterSet):
    """FilterSet for Challenges."""

    class Meta:
        model = Challenge
        fields = (
            "is_conveyable",
            "tags",
        )
