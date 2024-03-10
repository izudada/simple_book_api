from rest_framework.test import APIClient
from django.urls import reverse


client = APIClient()

def register_and_login_client():
    """
        AN authentication test helper
    """
    client.post(reverse('register'), {
        "username": "armani",
        "first_name": "John",
        "last_name": "Jack",
        "email": "armani@gmail.com",
        "password": "password1234@#"
    })
    response = client.post(
        reverse('login'), 
        {'email': 'armani@gmail.com', 'password': 'password1234@#'
    })
    token = response.data['token']
    assert response.status_code == 200, f"Login failed: {response.content}"
    return token

def create_book_object():
    """
        An test herlper to create a book object
    """
    token = register_and_login_client()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token }')
    response = client.post('http://localhost:8000/api/v1/books/', {
        "title": "test book",
        "author": "test author",
        "publication_date": "2024-03-09T12:00:00",
        "isbn": "0-061-96436-0",
        "genre": "ROM",
        "price": 10000,
        "stock": 7
    })
    return response