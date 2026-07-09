from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Student, course
from .forms import StudentForm
from django.db.models import Avg
from django.contrib import messages

# Create your views here.
def home(request):
    total_students = Student.objects.count()
    total_departments = Department.objects.count()
    total_courses = course.objects.count()
    average_cgpa = Student.objects.aggregate(Avg('cgpa'))['cgpa__avg']

    context = {
        'total_students': total_students,
        'total_departments': total_departments,
        'total_courses': total_courses,
        'average_cgpa':  round(average_cgpa, 2) if average_cgpa else 0.00,
    }
    return render(request, 'home.html', context)

def student_list(request):
    search = request.GET.get('search')
    students = Student.objects.all()
    if search:
        students = students.filter(first_name__icontains=search) | students.filter(last_name__icontains=search) | students.filter(email__icontains=search)
    students = students.order_by('user__first_name', 'user__last_name')
    context = {
        'students': students,
        'search': search,
    }

    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    context = {
        'student': student,
    }

    return render(request, 'students/student_detail.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form, 'title': 'Create Student'})

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form, 'student': student, 'title': 'Update Student'})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')

    return render(request, 'students/student_delete.html', {'student': student, 'title': 'Delete Student'})