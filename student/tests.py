from django.test import TestCase
from django.urls import reverse

from .models import Course, Department, student


class StudentViewsTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Computer Science', building='Block A')
        self.course = Course.objects.create(name='Django Basics', department=self.department)
        self.student = student.objects.create(
            first_name='Alice',
            last_name='Johnson',
            email='alice@example.com',
            phone='1234567890',
            dob='2000-01-01',
            gender='FEMALE',
            department=self.department,
            course=self.course,
        )

    def test_student_list_page_loads(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)

    def test_student_detail_page_loads(self):
        response = self.client.get(reverse('student_detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 200)

    def test_student_create_page_loads(self):
        response = self.client.get(reverse('student_create'))
        self.assertEqual(response.status_code, 200)

    def test_student_can_be_created_via_form(self):
        payload = {
            'first_name': 'Bob',
            'last_name': 'Smith',
            'email': 'bob@example.com',
            'phone': '1234567890',
            'dob': '2001-02-03',
            'gender': 'MALE',
            'department': self.department.id,
            'course': self.course.id,
        }
        response = self.client.post(reverse('student_create'), payload, follow=True)
        self.assertRedirects(response, reverse('student_list'))
        self.assertTrue(student.objects.filter(email='bob@example.com').exists())
