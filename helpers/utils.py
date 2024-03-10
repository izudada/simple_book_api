import re

from django.core.exceptions import ValidationError


def validate_isbn(value):
    """
    Validate the ISBN is either in ISBN-10 or ISBN-13 format.
    This is a basic validation to check the format only.
    """
    # Remove hyphens and spaces
    isbn = value.replace('-', '').replace(' ', '')

    # Check length
    if len(isbn) not in [10, 13] or not isbn.isdigit():
        raise ValidationError(f'{value} is not a valid ISBN number.')