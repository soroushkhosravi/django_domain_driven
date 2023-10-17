"""The fixtures usable in the tests."""
from django.test import Client
import pytest

@pytest.fixture
def client():
    """An app client for the tests."""
    return Client()
