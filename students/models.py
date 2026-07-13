from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
    
    
