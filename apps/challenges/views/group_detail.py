from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import ChallengeGroup


class ChallengeGroupDetailView(LoginRequiredMixin, DetailView):
    """Challenge Group detail view."""

    model = ChallengeGroup
    queryset = ChallengeGroup.objects.select_related("owner")
    context_object_name = "group"

    template_name = "challenges/challenge_group_detail.html"
