from http.client import HTTPResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from .. import forms, models


class ChallengeGroupCreateView(LoginRequiredMixin, CreateView):
    """Challenge group creating view."""

    model = models.ChallengeGroup
    form_class = forms.ChallengeGroupForm
    template_name = "challenges/challenge_group_create.html"

    def form_valid(self, form) -> HTTPResponse:
        """Set `owner` field to group and add group to favorite."""
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        self.request.user.favorite_groups.add(self.object)
        return response

    def get_success_url(self) -> str:
        """Return new group page url after creating."""
        return reverse("groups:group-detail", args=(self.object.id,))
