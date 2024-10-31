from rest_framework import serializers
from student.models import Student
from classroom_period.models import ClassroomPeriod
from classes.models import Class
from course.models import Course
from teacher.models import Teacher
from datetime import datetime,date

class StudentSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer()

    class Meta:
        model = Student
        fields = '__all__'

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"

    def get_age(self, object):
        if not object.date_of_birth:
            return None  # or return a default value, e.g., 0
        today = datetime.now()
        date_of_birth = object.date_of_birth
        if isinstance(date_of_birth, date) and not isinstance(date_of_birth, datetime):
            date_of_birth = datetime.combine(date_of_birth, datetime.min.time())
        age = today - date_of_birth
        return age.days // 365

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'email', 'full_name', 'age']  # Include 'full_name' and 'age' in fields


class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)  # Change 'teachers' to 'students'
    class Meta:
        model = Teacher
        fields = '__all__'
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'classroom','country']


class CoursesSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Change 'first_name' to 'teacher'
    class Meta:
        model = Course
        fields = '__all__'

class ClassroomPeriodSerializer(serializers.ModelSerializer):
     class Meta:
          model = ClassroomPeriod
          fields = "__all__"

        
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_title','course_materials']

class ClassesSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    teacher = TeacherSerializer()
    class Meta:
        model = Class
        fields = '__all__' 
       
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name','class_capacity','teacher']


class MinimalClassroomPeriodSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = ClassroomPeriod
        fields = '__all__'

class MinimalClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomPeriod
        fields = ['id', 'classroom','day_of_the_week']