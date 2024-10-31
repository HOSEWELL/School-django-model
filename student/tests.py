from django.test import TestCase
from .models import Student
from .forms import StudentRegistrationForm


# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        self.student= Student(
            first_name="Queen",
            last_name ="Bella",
            code="035",
            email ="umurerwaqueenbella",
            phone_number ="+250780768445",
        )

    # def test_full_name_contains_first_name(self):
    #     self.assertIn(self.student.first_name, self.student.full_name())
        
    # def test_full_name_contains_last_name(self):
    #     self.assertIn(self.student.last_name, self.student.full_name())     

class StudentFormTest(TestCase):
    # def test_student_form_valid(self):
    #     form_data={
    #         'first_name':'Glory',
    #         'last_name':'Maina'
    #     }
    #     form=StudentRegistrationForm(data=form_data)
    #     self.assertTrue(form.is_valid())

    def test_student_form_invalid(self):
        form_data={
            'first_name':'Glory',
            'last_name':'Maina'
        }
        form=StudentRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())