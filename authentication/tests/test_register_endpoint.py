from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from authentication.models import User


class TestRegisterAPI(APITestCase):
    def setUp(self):
        self.url = reverse('register')
        self.payload = {
            "username": "foobar",
            "first_name": "Foo",
            "last_name": "Bar",
            "email": "foobar@gmail.com",
            "password": "password1234@#"
        }

    def test_register_usersucceeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 200
        """
        #   assertion before registring
        self.assertFalse(User.objects.filter(username=self.payload['username']).exists())
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #   assertion after registring
        self.assertTrue(User.objects.filter(username=self.payload['username']).exists())
        
    def test_update_book_with_existing_email_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns email field error
        """
        user = User.objects.create(
            username="arcane",
            first_name="John",
            last_name="Jack",
            email="arcane@gmail.com",
            password="password1234@#"
        )
        user.save()
        self.payload['email'] = user.email
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.json()['email'], ['user with this email address already exists.'])


