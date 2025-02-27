from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # You can add custom fields here if needed
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
