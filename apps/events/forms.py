from django import forms

from apps.challenges.models import ChallengeGroup
from apps.users.models import User

from .models import Event


class EventForm(forms.ModelForm):
    """Form for `Event` model."""

    challenge_groups = forms.ModelMultipleChoiceField(
        queryset=ChallengeGroup.objects.all(),
    )
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
    )

    class Meta:
        model = Event
        fields = (
            "title",
            "challenge_groups",
            "members",
        )
