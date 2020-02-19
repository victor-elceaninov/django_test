from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.utils import json


class BaseViewTest(APITestCase):
    client = APIClient()

    def register_a_user(self, first_name="", last_name="",
                        username="", email="", password=""):
        return self.client.post(
            reverse("register", kwargs={"version": "v1"}),
            data=json.dumps(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "email": email,
                    "password": password,
                }
            ),
            content_type='application/json'
        )

    def login_a_user(self, username="", password=""):
        return self.client.post(
            reverse("login", kwargs={"version": "v1"}),
            data=json.dumps({
                "username": username,
                "password": password,
            }),
            content_type='application/json'
        )

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="User",
        )


class UserCreateTest(BaseViewTest):
    """
    This test ensures that a new user can be registered.
    Endpoint /auth/register/
    """
    def test_create_user_success(self):
        response = self.register_a_user("first_name",
                                        "last_name",
                                        "username",
                                        "email@email.email",
                                        "password")
        # assert status code is 201 CREATED
        self.assertEqual(response.data["user"]["first_name"], "first_name")
        self.assertEqual(response.data["user"]["last_name"], "last_name")
        self.assertEqual(response.data["user"]["username"], "username")
        self.assertEqual(response.data["user"]["email"], "email@email.email")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """
    This test ensures that User doesn't provide all required fields.
    """
    def test_create_user_data_required(self):
        response = self.register_a_user()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTest(BaseViewTest):
    """
    This test ensures that User has logged in correctly.
    Endpoint /auth/login/
    """
    def test_login_success(self):
        response = self.login_a_user("test_user", "testing")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This test ensures that User has provided wrong credentials.
    Endpoint /auth/login/
    """
    def test_login_error(self):
        response = self.login_a_user("test_user", "password")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
