import factory

from apps.users.factories import UserFactory

from ..models import Challenge


class ChallengeFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Challenge model."""

    title = factory.Faker("company")
    description = factory.Faker("text")
    prize = factory.Faker("name")

    is_conveyable = True
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Challenge
