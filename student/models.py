from django.db import models
from django.conf import settings 

class Department(models.Model):
    name = models.CharField(max_length=100)
    building=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(models.Model):

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
        ('prefer not to say', 'Prefer not to say')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    related_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cgpa = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"