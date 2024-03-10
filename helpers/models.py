import uuid

from django.db import models
from django.utils import timezone


def generate_id():
    return uuid.uuid4().hex


class TrackingModel(models.Model):
    id = models.CharField(
        max_length=60, primary_key=True, default=generate_id, editable=False
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)