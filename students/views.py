from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Student, Department, course
from .forms import StudentForm
from accounts.mixins import AdminRequiredMixin, TeacherRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_students"] = Student.objects.count()
        context["total_departments"] = Department.objects.count()
        context["total_courses"] = course.objects.count()

        context["average_cgpa"] = (
            Student.objects.aggregate(Avg("cgpa"))["cgpa__avg"] or 0
        )

        return context


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"

    def get_queryset(self):

        queryset = Student.objects.select_related(
            "user",
            "department"
        ).prefetch_related("courses")

        search = self.request.GET.get("search")

        if search:
            queryset = queryset.filter(
                user__first_name__icontains=search
            )

        return queryset.order_by("user__first_name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"
    pk_url_kwarg = "student_id"


class StudentCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        messages.success(self.request, "Student Added Successfully")
        return super().form_valid(form)

    


class StudentUpdateView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")
    pk_url_kwarg = "student_id"

    def form_valid(self, form):
        messages.success(self.request, "Student Updated Successfully")
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student_list")
    pk_url_kwarg = "student_id"

    def form_valid(self, form):
        messages.success(self.request, "Student Deleted Successfully")
        return super().form_valid(form)

home = HomeView.as_view()
student_list = StudentListView.as_view()
student_detail = StudentDetailView.as_view()
student_create = StudentCreateView.as_view()
student_update = StudentUpdateView.as_view()
student_delete = StudentDeleteView.as_view()