from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'dob',
            'gender',
            'department',
            'course',
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = Student.objects.filter(email=email)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone number must be a 10-digit number.")
        return phone