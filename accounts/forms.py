from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser
from students.models import Student, Department, course


class RegisterForm(UserCreationForm):

    dob = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    gender = forms.ChoiceField(
        choices=Student.gender_choices
    )

    cgpa = forms.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all()
    )

    courses = forms.ModelMultipleChoiceField(
        queryset=course.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    photo = forms.ImageField(
        required=False
    )

    class Meta:

        model = CustomUser

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
            "profile_picture",
            "password1",
            "password2",
        )

    @transaction.atomic
    def save(self, commit=True):

        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.role = self.cleaned_data["role"]

        if self.cleaned_data.get("profile_picture"):
            user.profile_picture = self.cleaned_data["profile_picture"]

        if commit:
            user.save()

            student = Student.objects.create(
                user=user,
                dob=self.cleaned_data["dob"],
                gender=self.cleaned_data["gender"],
                cgpa=self.cleaned_data["cgpa"],
                department=self.cleaned_data["department"],
                photo=self.cleaned_data.get("photo")
            )

            student.courses.set(
                self.cleaned_data["courses"]
            )

        return user