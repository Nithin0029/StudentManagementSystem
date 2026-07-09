from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from students.models import Student, Department, Course
from django.db import transaction



class RegistrationForm(UserCreationForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Student.gender_choices)
    department = forms.ModelChoiceField(queryset=None)
    courses = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
    photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name', 'email', 'phone', 'password1', 'password2']


    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.phone=self.cleaned_data['phone']
        user.role=self.cleaned_data['role']
        if self.cleaned_data['profile_picture']:
            user.profile_picture=self.cleaned_data['profile_picture']
        if commit:
            user.save()
            student = Student.objects.create(
                user=user,
                dob=self.cleaned_data['dob'],
                gender=self.cleaned_data['gender'],
                cgpa=self.cleaned_data['cgpa'],
                photo=self.cleaned_data['photo'],
                department=self.cleaned_data['department']
            )
            student.courses.set(self.cleaned_data['courses'])

        return user