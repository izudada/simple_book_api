from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from authentication.models import User
from book.contest import register_and_login_client

class TestLoginAPI(APITestCase):
    def setUp(self):
        self.data = register_and_login_client()
        self.url = reverse('login')
        self.payload = {
        "email": "armani@gmail.com",
            "password": "password1234@#"
        }

    def test_login_user_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 200
        """
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #   assertion after registring
        self.assertTrue(self.payload['email'], response.json()['email'])
        self.assertIn('token',response.json())
        
    def test_user_login_with_invalid_credentials_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns email field error
        """

        self.payload['email'] = 'user@no'
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()['error'], 'invalid user')
