from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            
            
            'dob',
            'gender',
            'photo',
            'department',
            'courses',
            'cgpa',
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'courses': forms.CheckboxSelectMultiple(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance and self.instance.pk:
            if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This email is already in use.")
        else:
            if Student.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be a 10-digit number.")
        return phone_number

    def clean_cgpa(self):
        cgpa = self.cleaned_data.get('cgpa')
        if cgpa is not None and (cgpa < 0 or cgpa > 10):
            raise forms.ValidationError("CGPA must be between 0 and 10.")
        return cgpa