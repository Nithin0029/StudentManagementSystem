from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher')
    )
    phone=models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')