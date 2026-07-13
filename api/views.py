from rest_framework import generics

from students.models import Student

from .serializers import (
    StudentSerializer,
    StudentWriteSerializer,
)
from rest_framework.permissions import IsAuthenticated

class StudentListCreateAPI(generics.ListCreateAPIView):

    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):

        if self.request.method == "POST":
            return StudentWriteSerializer

        return StudentSerializer


class StudentRetrieveUpdateDestroyAPI(
    generics.RetrieveUpdateDestroyAPIView
):
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.select_related(
        "user",
        "department"
    ).prefetch_related("courses")

    def get_serializer_class(self):

        if self.request.method in ["PUT", "PATCH"]:
            return StudentWriteSerializer

        return StudentSerializer