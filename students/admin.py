from django.contrib import admin
from students.models import Student
from students.models import Student, Department, course

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'dob', 'gender','photo', 'department')
   

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code' )
    search_fields = ('name','code')


@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits')
    search_fields = ('name','code')

