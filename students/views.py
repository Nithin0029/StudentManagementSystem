from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all().order_by('first_name')

    context = {
        'students': students,
    }

    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    context = {
        'student': student,
    }

    return render(request, 'students/student_detail.html', context)