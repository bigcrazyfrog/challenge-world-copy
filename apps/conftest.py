# pylint: disable=cannot-enumerate-pytest-fixtures

from django.test import Client

from rest_framework import test

import pytest

from .users.factories import UserFactory
from .users.models import User


@pytest.fixture
def api_client() -> test.APIClient:
    """Create api client."""
    return test.APIClient()


@pytest.fixture(scope="module")
def user(django_db_blocker) -> User:
    """Create user for testing."""
    with django_db_blocker.unblock():
        return UserFactory()


@pytest.fixture
def auth_client(user: User, client: Client) -> Client:
    """Create authorized client for tests."""
    client.force_login(user)
    return client
