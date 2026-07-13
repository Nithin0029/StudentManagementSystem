from django import forms
from django.contrib.auth import get_user_model
from .models import Student

User = get_user_model()

class StudentForm(forms.ModelForm):
    user=forms.ModelChoiceField(
        queryset=User.objects.filter(role='STUDENT'),
        empty_label="Select a student",
        required=False,
    )
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Student
        fields = [
            'dob',
            'gender',
            'cgpa',
            'photo',
            'department',
            'courses',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['phone_number'].initial = self.instance.user.phone_number
            self.fields['user'].initial = self.instance.user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_query = User.objects.filter(email=email)
        if self.instance and self.instance.pk and self.instance.user:
            user_query = user_query.exclude(pk=self.instance.user.pk)
        if user_query.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise forms.ValidationError("Phone number must be a 10-digit number.")
        return phone_number

    def save(self, commit=True):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        user = self.cleaned_data.get('user')

        if self.instance and self.instance.pk and self.instance.user:
            user = self.instance.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            user.save()
        elif user:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            user.save()
            self.instance.user = user
        else:
            username = email.split('@')[0]
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                role='STUDENT'
            )
            self.instance.user = user

        return super().save(commit=commit);