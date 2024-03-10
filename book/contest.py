from rest_framework.test import APIClient
from django.urls import reverse

def register_and_login_client():
    """
        AN authentication test helper
    """
    client = APIClient()
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
