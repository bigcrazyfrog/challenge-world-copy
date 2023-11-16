from django_filters.views import FilterView

from ..filters import ChallengeFilter
from ..models import Achievement, Challenge


class ChallengeListView(FilterView):
    """Challenge list view."""

    paginate_by = 50
    model = Challenge
    template_name = "challenges/challenge_list.html"
    context_object_name = "challenges"
    filterset_class = ChallengeFilter

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_anonymous:
            return context

        approved_challenges = Achievement.objects.select_related(
            "user",
        ).filter(
            user=self.request.user,
            is_approved=True,
        ).distinct(
            "challenge",
        ).values_list("challenge__id", flat=True)

        not_approved_challenges = Achievement.objects.select_related(
            "user",
        ).filter(
            user=self.request.user,
            is_approved=False,
        ).distinct(
            "challenge",
        ).values_list("challenge__id", flat=True)

        context.update(
            {
                "completed_challenges": approved_challenges,
                "not_approved_challenges": not_approved_challenges,
            },
        )
        return context
