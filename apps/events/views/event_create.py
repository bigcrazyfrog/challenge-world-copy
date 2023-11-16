from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView

from ..forms import EventForm
from ..models import Event


class EventCreateView(LoginRequiredMixin, CreateView):
    """Event create view."""

    model = Event
    template_name = "events/event_create.html"
    form_class = EventForm

    def form_valid(self, form: EventForm) -> HttpResponse:
        """If the form is valid, save challenge model."""
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse(
            "event-detail",
            args=(
                self.object.id,
            ),
        )
