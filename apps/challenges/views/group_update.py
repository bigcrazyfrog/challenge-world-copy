from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.views.generic import UpdateView

from ..forms import ChallengeGroupForm
from ..models import ChallengeGroup


class ChallengeGroupUpdateView(LoginRequiredMixin, UpdateView):
    """Challenge group updating view."""

    model = ChallengeGroup
    form_class = ChallengeGroupForm

    template_name = "challenges/challenge_group_update.html"

    def get_queryset(self) -> QuerySet[ChallengeGroup]:
        return super().get_queryset().filter(owner=self.request.user)

    def get_success_url(self) -> str:
        """Return group page url after updating."""
        return reverse("groups:group-detail", args=(self.object.id,))
