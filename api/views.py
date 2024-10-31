from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from student.models import Student
from classes.models import Class
from .serializers import StudentSerializer
from classroom_period.models import ClassroomPeriod
from .serializers import ClassroomPeriodSerializer
from .serializers import ClassesSerializer
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from .serializers import MinimalStudentSerializer
from .serializers import TeacherSerializer
from .serializers import MinimalCourseSerializer
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalClassroomSerializer
from .serializers import MinimalClassroomPeriodSerializer
class StudentView(APIView):
    def get(self,request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if country:
            students = students.filter(country = country)
        if first_name:
            students = students.filter(first_name = first_name)

        serializer = MinimalStudentSerializer(students,many=True)
        return Response(serializer.data)
    

    def post(self, request, id):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomPeriodView(APIView):
    def get(self,request):
        classperiods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(classperiods,many=True)
        serializer = MinimalClassroomPeriodSerializer(classperiods, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
class ClassesView(APIView):
    def get(self,request):
        classess = Class.objects.all()
        serializer = ClassesSerializer(classess,many=True)
        serializer= MinimalClassroomSerializer(classess, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CoursesView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CoursesSerializer(courses,many=True)
        serializer=MinimalCourseSerializer(courses,many=True)
        return Response(serializer)
    def post(self, request):
        serializer = CoursesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeachersView(APIView):
    def get(self,request):
        courses = Teacher.objects.all()
        serializer =TeacherSerializer(courses,many=True)
        serializer=MinimalTeacherSerializer(courses,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetailView(APIView):
    def enroll(self, student,course_id):
        course = Course.objects.get(id= course_id)
        student.courses.add(course)
        
    def post(self, request, id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")
        if action=="enroll":
            course_id = request.data.get("course_id")
            self.enroll(Student, course_id)
        return Response(status=status.HTTP_201_CREATED)
    
    def get (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)
    def add_to_class(self, student, class_id):
        student_class = Class.objects.get(id=class_id)
        student_class.students.add(student)
    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)
    

class TeacherDetailView(APIView):
    def get (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  

class ClassDetailView(APIView):
    def get (self, request,id):
        classes= Class.objects.get(id = id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    def put (self, request,id):
        classes = Class.objects.get(id = id)
        serializer = StudentSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classes = Class.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED) 
    
class CourseDetailView(APIView):
    def get (self, request,id):
        course = Courses.objects.get(id = id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    def put (self, request,id):
        course = Courses.objects.get(id = id)
        serializer = StudentSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        course = Student.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassroomPeriodDetailView(APIView):
    def get (self, request,id):
        classrom_period = ClassroomPeriod.objects.get(id = id)
        serializer = ClassroomPeriodSerializer(classrom_period)
        return Response(serializer.data)
    def put (self, request,id):
        classroom_period = ClassroomPeriod.objects.get(id = id)
        serializer = ClassroomPeriodSerializer(classroom_period,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classroom_period = ClassroomPeriod.objects.get(id = id)
        classroom_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassroomPeriod.objects.all()
        serializer = ClassroomPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)