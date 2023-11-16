from django import forms

from . import models


class ChallengeGroupForm(forms.ModelForm):
    """Form for `ChallengeGroup` model with `challenges` extra field."""

    challenges = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Challenge.objects,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = models.ChallengeGroup
        fields = (
            "title",
            "is_public",
            "challenges",
        )


class ChallengeForm(forms.ModelForm):
    """Form for `Challenge` model."""

    tags = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(),
        required=False,
    )

    class Meta:
        model = models.Challenge
        fields = (
            "title",
            "description",
            "prize",
            "is_conveyable",
            "tags",
        )
