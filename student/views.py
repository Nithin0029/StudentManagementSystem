from django.shortcuts import redirect, render, get_object_or_404

from student.forms import StudentForm
from .models import Department, Course, Student


def home(request):
    total_students = Student.objects.count()
    total_departments = Department.objects.count()
    total_courses = Course.objects.count()
    average_cgpa = 0

    context = {
        'total_students': total_students,
        'total_departments': total_departments,
        'total_courses': total_courses,
        'average_cgpa': average_cgpa,
    }
    return render(request, 'home.html', context)


def student_list(request):
    search = request.GET.get('search', '')
    if search:
        students = Student.objects.filter(first_name__icontains=search)
    else:
        students = Student.objects.all().order_by('first_name')

    context = {
        'students': students,
        'search': search
    }

    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student_record = get_object_or_404(Student, id=student_id)

    context = {
        'student': student_record
    }

    return render(request, 'students/student_detail.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_obj = form.save(commit=False)
            if not student_obj.user_id:
                from django.contrib.auth import get_user_model
                user_model = get_user_model()
                username = f"student_{student_obj.email.split('@')[0]}"
                user = user_model.objects.create_user(
                    username=username,
                    email=student_obj.email,
                    password='Student@123'
                )
                student_obj.user = user
            student_obj.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Create Student'})




def student_update(request, student_id):
    student_obj = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student_obj)

    return render(request, 'students/student_form.html', {'form': form, 'title': 'Update Student'})

def student_delete(request, student_id):
    student_obj = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student_obj.delete()
        return redirect('student_list')
    return render(request, 'students/student_delete.html', {'student': student_obj})