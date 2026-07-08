from django.contrib import admin

from .models import Course, Department, student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'building')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('name',)


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department', 'gender')
    list_filter = ('department', 'gender')
    search_fields = ('first_name', 'last_name', 'email')