from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username