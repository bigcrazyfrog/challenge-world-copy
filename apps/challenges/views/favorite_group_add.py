from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ..models import ChallengeGroup


class FavoriteGroupAddView(UpdateView):
    """Add group to favorite view."""

    model = ChallengeGroup
    fields = ()

    template_name = "challenges/favorite_group_add.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.request.user.favorite_groups.add(self.object)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("groups:group-detail", args=(self.object.pk,))
