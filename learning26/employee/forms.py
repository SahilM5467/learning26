from django import forms
from .models import Employee, Course, Car, Bike

class EmployeeeForm(forms.ModelForm):
    class Meta :
        model = Employee
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta :
        model = Course
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta :
        model = Car
        fields = '__all__'

class BikeForm(forms.ModelForm):
    class Meta :
        model = Bike
        fields = '__all__'







