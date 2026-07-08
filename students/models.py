from django.db import models

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
        return self.name

class Student(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    course = models.ManyToManyField(course)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
