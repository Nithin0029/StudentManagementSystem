from django.contrib import admin
from students.models import Student
from students.models import Student, Department, course

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'cgpa', 'department')
    list_filter = ('department', 'gender')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user_email')
    filter_horizontal = ('courses',)
   

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code' )
    search_fields = ('name','code')


@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits')
    search_fields = ('name','code')

