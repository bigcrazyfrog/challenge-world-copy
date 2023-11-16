import factory

from apps.users import factories

from . import models


class EventFactory(factory.django.DjangoModelFactory):
    """Factory to generate test `Event` instance."""

    title = factory.Faker("company")
    owner = factory.SubFactory(factories.UserFactory)

    class Meta:
        model = models.Event

    @factory.post_generation
    def members(self, create, extracted, **kwargs) -> None:
        """Post generation members field."""
        if not create or not extracted:
            return

        # pylint: disable=no-member
        self.members.add(*extracted)
