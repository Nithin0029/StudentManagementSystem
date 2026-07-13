from rest_framework import serializers
from students.models import Student, Department, course
from accounts.models import CustomUser
from rest_framework import generics 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "role",
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"
        
class courseSerializer(serializers.ModelSerializer):

    class Meta:
        model = course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    department = DepartmentSerializer(read_only=True)
    courses = courseSerializer(many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",

        ]


class StudentWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",
        ]

    def to_internal_value(self, data):
        data = data.copy()
        photo = data.get("photo")
        if photo and isinstance(photo, str):
            if photo.startswith("http://") or photo.startswith("https://") or photo.startswith("/media/"):
                data.pop("photo", None)
        return super().to_internal_value(data)

class StudentWriteSerializers(serializers.ModelSerializer):
    model = Student
    fields = [
            "id",
            "user",
            "dob",
            "gender",
            "cgpa",
            "photo",
            "department",
            "courses",
        ]

    def validate_cgpa(self, value):
        if not 0 < value > 10:
            raise serializers.ValidationError("CGPA must be between 0 and 10.")
        return value