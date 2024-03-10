from rest_framework.test import APITestCase
from rest_framework import status

from book.contest import create_book_object, register_and_login_client


class TestBookUpdateAPI(APITestCase):
    def setUp(self):
        self.data = create_book_object().data
        self.id = self.data.get('id')
        self.url = f'/api/v1/books/{self.id}/'
        self.token = register_and_login_client()
        self.payload = {
            "title": "Sample Book Title",
            "author": "John Doe",
            "publication_date": "2022-01-01",
            "isbn": "978-1-23456-789-0",
            "genre": "ROM",
            "price": 12000.0,
            "stock": 17
        }

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token }')

    def test_update_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 200
        """
        self.authenticate()

        #   assertion before update
        self.assertEqual(self.data.get('price'), 10000)
        response = self.client.put(self.url, self.payload)
        print(response, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #   assertion after update
        self.assertEqual(response.data.get('price'), 12000.0)

    def test_update_invalid_book_fails(self):
        """
            Test that an authenticated user hits the endpoint
            with an invalid bok id
            the request returns 404
        """
        self.authenticate()
        response = self.client.put('/api/v1/books/247305efecb147f99305/', self.payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_update_book_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns 403
        """
        response = self.client.put(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

