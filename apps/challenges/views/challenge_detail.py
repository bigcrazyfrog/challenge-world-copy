from django.views.generic import DetailView

from apps.challenges.models import Challenge


class ChallengeDetailView(DetailView):
    """Challenge detail view."""

    model = Challenge
    template_name = "challenges/challenge_detail.html"
    context_object_name = "challenge"
