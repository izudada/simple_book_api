from rest_framework.test import APITestCase
from rest_framework import status

from book.models import Book
from book.contest import create_book_object, register_and_login_client


class TestBookDeleteAPI(APITestCase):
    def setUp(self):
        self.data = create_book_object().data
        self.id = self.data.get('id')
        self.url = f'/api/v1/books/{self.id}/'
        self.token = register_and_login_client()

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token }')

    def test_update_succeeds(self):
        """
            Test that an authenticated user hits the endpoint
            the request returns 200
        """
        self.authenticate()


        #   assertion before deletion
        self.assertTrue(Book.objects.filter(id=self.id).exists())
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        #   assertion after deletion
        self.assertFalse(Book.objects.filter(id=self.id).exists())

    def test_update_invalid_book_fails(self):
        """
            Test that an authenticated user hits the endpoint
            with an invalid bok id
            the request returns 404
        """
        self.authenticate()
        response = self.client.delete('/api/v1/books/247305efecb147f99305/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_update_book_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns 403
        """
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

