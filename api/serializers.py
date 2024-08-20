from rest_framework import serializers
from student.models import Student
from classroom_period.models import ClassroomPeriod
from classes.models import Class
from course.models import Courses
from teacher.models import Teacher
from datetime import datetime

class CoursesSerializer(serializers.ModelSerializer):
     class Meta:
          model = Courses
          fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_title','course_materials']

class StudentSerializer(serializers.ModelSerializer):
     courses = CoursesSerializer(many = True)
     class Meta:
          model = Student
          # fields = "__all__"
          exclude = ["email"]

class ClassroomPeriodSerializer(serializers.ModelSerializer):
     class Meta:
          model = ClassroomPeriod
          fields = "__all__"


class MinimalClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomPeriod
        fields = ['id', 'course','day_of_the_week']
class ClassesSerializer(serializers.ModelSerializer):
     class Meta:
          model = Class
          fields = "__all__"
     
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name','class_capacity']




class TeacherSerializer(serializers.ModelSerializer):
     class Meta:
          model = Teacher
          fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'classroom','country']


class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name =serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    def get_full_name(self, object):
         return f"{object.first_name} {object.last_name}"
    def get_age(self,object):
         today = datetime.now()
         age = today-object.date_of_birth
         return age
    
    class Meta:
        model = Student
        fields = ["id","full_name","age", "email"]