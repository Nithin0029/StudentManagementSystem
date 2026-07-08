from django.shortcuts import render,get_object_or_404
from .models import student

def home(request):
    return render(request, 'home.html')

def student_list(request):
    students=student.objects.all().order_by('first_name')

    context={
        'students': students
    }

    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student_record = get_object_or_404(student, id=student_id)

    context = {
        'student': student_record
    }

    return render(request, 'students/student_detail.html', context)