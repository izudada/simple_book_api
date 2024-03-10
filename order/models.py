from django.db import models

from authentication.models import User
from helpers.models import TrackingModel


class Order(TrackingModel, models.Model):

    author = models.CharField(max_length=150)
    meta_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order for {self.user.username}"
