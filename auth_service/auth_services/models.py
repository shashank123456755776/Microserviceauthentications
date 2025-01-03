import uuid
import secrets
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('project_manager', 'Project Manager'),
        ('team_member', 'Team Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='team_member')
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    api_key = models.CharField(max_length=64, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = secrets.token_hex(32)  # Generates a 64-character secure API key
        super().save(*args, **kwargs)
