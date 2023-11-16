from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import UpdateView

from ..forms import EventForm
from ..models import Event


class EventUpdateView(LoginRequiredMixin, UpdateView):
    """Event update view."""

    model = Event
    template_name = "events/event_update.html"
    form_class = EventForm

    def get_success_url(self) -> str:
        return reverse(
            "event-detail",
            args=(
                self.object.id,
            ),
        )
