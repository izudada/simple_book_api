from rest_framework.test import APITestCase
from rest_framework import status


class TestRegisterAPI(APITestCase):
    def setUp(self):
        self.url = f'/api/v1/register'
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
        self.authenticate()

        #   assertion before update
        self.assertEqual(self.data.get('price'), 10000)
        response = self.client.put(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #   assertion after update
        self.assertEqual(response.data.get('price'), 12000.0)
        
    def test_update_book_without_auth_fails(self):
        """
            Test that an unauthenticated user hits the endpoint
            the request returns 403
        """
        response = self.client.put(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

