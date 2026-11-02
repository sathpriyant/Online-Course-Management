from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import JsonResponse


class CourseView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "course_name": "Python Full Stack",
                "duration": "6 Months",
                "fee": 45000,
                "description": "Full stack development using Python and Django",
                "instructor": "Arun"
            },
            {
                "id": 2,
                "course_name": "Flutter Development",
                "duration": "4 Months",
                "fee": 35000,
                "description": "Mobile application development",
                "instructor": "Rahul"
            }
        ]
        return JsonResponse(data, safe=False)


class InstructorView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "name": "Arun",
                "email": "arun@gmail.com",
                "phone": "9876543210",
                "specialization": "Python and Django"
            },
            {
                "id": 2,
                "name": "Rahul",
                "email": "rahul@gmail.com",
                "phone": "9876543211",
                "specialization": "Flutter Development"
            }
        ]
        return JsonResponse(data, safe=False)


class StudentView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "name": "Akhil",
                "email": "akhil@gmail.com",
                "phone": "9876543212",
                "place": "Kochi",
                "qualification": "BCA"
            },
            {
                "id": 2,
                "name": "Vishnu",
                "email": "vishnu@gmail.com",
                "phone": "9876543213",
                "place": "Calicut",
                "qualification": "BSc Computer Science"
            }
        ]
        return JsonResponse(data, safe=False)


class EnrollmentView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "student_id": 1,
                "course_id": 1,
                "enrollment_date": "2026-10-15",
                "status": "Active"
            },
            {
                "id": 2,
                "student_id": 2,
                "course_id": 2,
                "enrollment_date": "2026-10-20",
                "status": "Completed"
            }
        ]
        return JsonResponse(data, safe=False)


class LessonView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "lesson_name": "Python Basics",
                "course_id": 1,
                "duration": "2 Hours",
                "description": "Introduction to Python programming"
            },
            {
                "id": 2,
                "lesson_name": "Django Introduction",
                "course_id": 1,
                "duration": "3 Hours",
                "description": "Introduction to Django framework"
            },
            {
                "id": 3,
                "lesson_name": "Flutter Basics",
                "course_id": 2,
                "duration": "2 Hours",
                "description": "Introduction to Flutter development"
            }
        ]
        return JsonResponse(data, safe=False)
