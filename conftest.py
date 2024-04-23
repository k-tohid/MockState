import pytest

from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    """Django test client fixture."""
    return Client()


@pytest.fixture
def user_info():
    """return the user info that was used to create a user"""
    user_info = {
        'username': 'test_username',
        'password': 'test_password',
        'gender': 'male',
        'age': 20,
    }
    return user_info


@pytest.fixture
def customuser(client, user_info):
    """Create a custom user fixture through api"""

    url = reverse('user_create')
    response = client.post(url, user_info, format='json')

    user = response.json()
    return user
