import pytest

from django.test import Client
from django.urls import reverse

from rest_framework import status

from users.models import CustomUser


@pytest.fixture
def client():
    """Django test client fixture."""
    return Client()


@pytest.fixture
def customuser(client):
    """Create a custom user fixture through api"""

    user_info = {
        'username': 'test_username',
        'password': 'test_password',
        'gender': 'male',
        'age': 20,
    }

    url = reverse('user_create')
    response = client.post(url, user_info, format='json')

    user = response.json()
    return user
