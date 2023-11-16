import factory

from apps.users.factories import UserFactory

from ..models import ChallengeGroup


class ChallengeGroupFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Challenge group model."""

    title = factory.Faker("company")
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = ChallengeGroup
