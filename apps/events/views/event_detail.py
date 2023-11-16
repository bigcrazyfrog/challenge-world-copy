from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from apps.challenges.models import Achievement

from ..models import Event
from ..queryset import EventQuerySet


class EventDetailView(LoginRequiredMixin, DetailView):
    """Event detail view."""

    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_queryset(self) -> EventQuerySet:
        return super().get_queryset().available_for_user(
            user=self.request.user,
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        members = self.object.members.all()
        challenge_groups = self.object.challenge_groups.prefetch_related(
            "challenges",
        ).union(
            self.request.user.favorite_groups.prefetch_related("challenges"),
        )
        moderators = self.object.moderators.all()
        completed_challenges = Achievement.objects.select_related(
            "challenge",
            "event",
            "user",
        ).filter(
            event=self.object,
            user=self.request.user,
            is_approved=True,
        ).values_list("challenge__id", flat=True)

        not_approved_challenges = Achievement.objects.select_related(
            "challenge",
            "event",
            "user",
        ).filter(
            event=self.object,
            user=self.request.user,
            is_approved=False,
        ).values_list("challenge__id", flat=True)

        context.update(
            {
                "members": members,
                "challenge_groups": challenge_groups,
                "moderators": moderators,
                "completed_challenges": completed_challenges,
                "not_approved_challenges": not_approved_challenges,
            },
        )
        return context
