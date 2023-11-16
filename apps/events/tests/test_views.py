# pylint: disable=cannot-enumerate-pytest-fixtures

from django.test import Client
from django.urls import reverse

from rest_framework import status

from apps.users.models import User

from .. import factories as event_factories


def test_event_detail(auth_client: Client, user: User) -> None:
    """Test event detail view."""
    event = event_factories.EventFactory(members=(user,))

    response = auth_client.get(
        reverse(
            "event-detail",
            args=(event.id,),
        ),
    )

    assert response.status_code == status.HTTP_200_OK
    assert user in response.context["members"]
