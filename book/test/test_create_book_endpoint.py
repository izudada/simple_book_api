from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from book.contest import register_and_login_client


class TestCreateBookAPI(APITestCase):
    def setUp(self):
        self.url = '/api/v1/books/'
        self.payload  = {
                "title": "Tipping point",
                "author": "Malcolm Gladwell",
                "publication_date": "2024-03-09T12:00:00",
                "isbn": "0-061-96436-0",
                "genre": "ROM",
                "price": 10000,
                "stock": 7
            }
        self.token = register_and_login_client()

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token }')

    def test_create_book_endpoint_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            with necessary payload
            the request returns 201
        """
        self.authenticate()
        response = self.client.post(self.url , self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_book_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            with necessary payload
            the request returns 403
        """
        response = self.client.post(self.url , self.payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

