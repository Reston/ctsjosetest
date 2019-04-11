import uuid
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return reverse('user:detail-user', uuid=str(self.uuid))
