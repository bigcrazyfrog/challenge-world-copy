from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView

from ..forms import ChallengeForm


class ChallengeCreateView(
    LoginRequiredMixin,
    CreateView,
):
    """Create new challenge view."""

    form_class = ChallengeForm
    template_name = "challenges/challenge_create.html"

    def get_success_url(self) -> str:
        """Return challenge page url after updating."""
        return reverse(
            "challenges:challenge-detail",
            args=(
                self.object.pk,
            ),
        )

    def form_valid(self, form: ChallengeForm) -> HttpResponse:
        """If the form is valid, save challenge model."""
        form.instance.author = self.request.user
        return super().form_valid(form)
