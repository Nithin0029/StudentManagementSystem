from django.urls import path

from .views import (
    StudentListCreateAPI,
    StudentRetrieveUpdateDestroyAPI,
)

urlpatterns = [

    path(
        "students/",
        StudentListCreateAPI.as_view(),
        name="student_api",
    ),

    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPI.as_view(),
        name="student_api_detail",
    ),

]