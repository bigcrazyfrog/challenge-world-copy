import factory

from ..models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Challenge tag model."""

    name = factory.Faker("name")

    class Meta:
        model = Tag
