from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )

    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, blank=True, null=True
    )
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
