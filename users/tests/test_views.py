import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

# from ..models import CustomUser


@pytest.mark.django_db
def test_create_custom_user(client):
    user_info = {
        'username': 'test_username',
        'password': 'test_password',
        'gender': 'male',
        'age': 20,
    }

    url = reverse('user_create')
    response = client.post(url, user_info, format='json')

    # Assert response status code and token key
    assert response.status_code == status.HTTP_201_CREATED
    assert "token" in response.data


# def test_retrieve_custom_user(client):
#     # Create a user
#     user = CustomUser.objects.create_user(username="test_user", password="test_password")

#     # Retrieve the user
#     url = reverse("customuser-detail", kwargs={"username": user.username})
#     response = client.get(url)

#     # Assert response status code
#     assert response.status_code == status.HTTP_200_OK


# def test_login_valid_credentials(client):
#     # Create a user
#     user = CustomUser.objects.create_user(username="test_user", password="test_password")

#     # Login with valid credentials
#     url = reverse("login")
#     data = {"username": "test_user", "password": "test_password"}
#     response = client.post(url, data, format="json")

#     # Assert response status code and token key
#     assert response.status_code == status.HTTP_200_OK
#     assert "token" in response.data


# def test_login_invalid_credentials(client):
#     # Attempt to login with invalid credentials
#     url = reverse("login")
#     data = {"username": "invalid_user", "password": "invalid_password"}
#     response = client.post(url, data, format="json")

#     # Assert response status code
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED