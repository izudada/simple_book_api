from django.db import models

from helpers.models import TrackingModel
from helpers.utils import validate_isbn


class Book(TrackingModel, models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science'),
        ('HIS', 'History'),
        ('FAN', 'Fantasy'),
        ('BIO', 'Biography'),
        ('THR', 'Thriller'),
        ('ROM', 'Romance'),
        ('OTHERS', 'Others')
    ]

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateTimeField()
    isbn = models.CharField(max_length=20, validators=[validate_isbn])
    genre = models.CharField(max_length=12, choices=GENRE_CHOICES)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    qty_left = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.qty_left = self.stock - self.qty_sold
        super(Book, self).save(*args, **kwargs) 