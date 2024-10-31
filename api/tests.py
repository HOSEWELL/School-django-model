from rest_framework import APITestCase
from student.models import Student
from django.urls import reverse
from rest_framework import status
from .serializers import StudentSerializer

# Create your tests here.

class StudentAPIViewTest(APITestCase):
     def setUp(self):
        self.student= Student.objects.create(
            first_name="Queen",
            last_name ="Bella",
            code="035",
            email ="umurerwaqueenbella",
            phone_number ="+250780768445",
        )

     def test_get_student_list(self):
         url = reverse('student_view')
         response = self.client_get(url)
         students = Student.objects.all()
         serializer = StudentSerializer(students, many = True)
         self.assertEqual(response.status.code, status.HTTP_200_OK)
         self.assertEqual(response.data, serializer.data)
    
