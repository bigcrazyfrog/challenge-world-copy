from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import CreateView

from apps.events.models import Event

from ..models import Achievement, Challenge


class ChallengeCompleteView(LoginRequiredMixin, CreateView):
    """Challenge complete view."""

    model = Achievement
    fields = (
        "event",
    )
    template_name = "challenges/challenge_complete.html"

    def get(
        self,
        request: HttpRequest,
        *args: str,
        **kwargs: Any,
    ) -> HttpResponseRedirect:
        """Register new achievement in event."""
        challenge_id = self.request.GET.get("challenge")
        event_id = self.request.GET.get("event")
        next_url = self.request.GET.get("next") or "/"

        challenge = Challenge.objects.filter(id=challenge_id).first()
        event = Event.objects.filter(id=event_id).first()

        if not event:
            return super().get(request, *args, **kwargs)

        if challenge is None:
            return HttpResponseRedirect(next_url)

        Achievement.objects.get_or_create(
            event=event,
            challenge=challenge,
            user=self.request.user,
        )

        return HttpResponseRedirect(next_url)

    def form_valid(self, form) -> HttpResponseRedirect:
        """If the form is valid, save challenge model."""
        challenge_id = self.request.GET.get("challenge")
        challenge = Challenge.objects.filter(id=challenge_id).first()
        next_url = self.request.GET.get("next") or "/"

        if challenge is None:
            return HttpResponseRedirect(next_url)

        Achievement.objects.get_or_create(
            event=form.instance.event,
            challenge=challenge,
            user=self.request.user,
        )

        return HttpResponseRedirect(next_url)
