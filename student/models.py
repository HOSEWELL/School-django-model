from django.db import models
# from course.models import Course

# Create your models here.

from datetime import date


class Student(models.Model):
    course = models.TextField()
    classroom = models.TextField() 
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=20)
    bio = models.TextField()
    # teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='students_assigned', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    def full_name(self):
        return f"{self.first_name} {self.last_name}" 
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    

 

   


        
