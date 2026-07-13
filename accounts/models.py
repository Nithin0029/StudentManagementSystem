from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # You can add custom fields here in the future if needed
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
    )
    
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')

    def __str__(self):
        return self.username