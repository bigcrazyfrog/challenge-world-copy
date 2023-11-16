import factory

from .models import Challenge


class ChallengeFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Challenge instance."""

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")
    prize = factory.Faker("text")

    class Meta:
        model = Challenge
