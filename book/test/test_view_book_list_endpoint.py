from rest_framework.test import APITestCase
from rest_framework import status

from book.contest import register_and_login_client


class TestListBookAPI(APITestCase):
    def setUp(self):
        self.url = '/api/v1/books/'
        self.token = register_and_login_client()

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token }')

    def test_list_book_endpoint_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 201
        """
        self.authenticate()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_list_book_endpoint_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns 403
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

