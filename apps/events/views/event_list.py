from django_filters.views import FilterView

from ..filters import EventFilter
from ..models import Event
from ..queryset import EventQuerySet


class EventListView(FilterView):
    """Event list view."""

    paginate_by = 5
    model = Event
    template_name = "events/event_list.html"
    filterset_class = EventFilter
    context_object_name = "events"

    def get_queryset(self) -> EventQuerySet:
        """Provide to show only public events if user is not login."""
        if self.request.user.is_anonymous:
            return Event.objects.filter(is_public=True)
        return super().get_queryset()
