from rest_framework.test import APITestCase
from rest_framework import status

from book.contest import create_book_object, register_and_login_client


class TestBookDetailAPI(APITestCase):
    def setUp(self):
        self.data = create_book_object().data
        self.id = self.data.get('id')
        self.url = f'/api/v1/books/{self.id}/'
        self.token = register_and_login_client()

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token }')

    def test_view_book_detail_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 200
        """
        self.authenticate()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.data.get('title'))
        self.assertEqual(response.data.get('id'), self.data.get('id'))

    def test_view_invalid_book_detail_fails(self):
        """
            Test that an authenticated user hits the endpoint
            with an invalid bok id
            the request returns 404
        """
        self.authenticate()
        response = self.client.get('/api/v1/books/247305efecb147f99305/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_view_book_detail_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns 403
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

