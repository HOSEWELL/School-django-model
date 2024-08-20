
from django.db import models
from teacher.models import Teacher
from student.models import Student

class Course(models.Model):
    course_id = models.IntegerField(default=1) 
    course_title = models.CharField(max_length=20)
    course_description = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    course_code = models.PositiveSmallIntegerField()
    course_materials = models.TextField()
    course_attendees = models.PositiveSmallIntegerField()
    course_fee = models.CharField(max_length=20)  

    # ForeignKey to Teacher
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses') 

    # ManyToMany relationship with Student
    students = models.ManyToManyField(Student, related_name='courses_enrolled', blank=True)

    def __str__(self):
        return f"{self.course_title} - {self.course_description}"
