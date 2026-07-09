from django.contrib import admin

from .models import Course, Department, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'building')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department', 'course')
    search_fields = ('first_name', 'last_name', 'email')