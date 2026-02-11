from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    post = models.CharField(max_length=50)
    join_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    position = models.CharField(max_length=50)

    class Meta:
        db_table = "employee_course"

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = "car"

    def __str__(self):
        return f"{self.name} - {self.company}"

class Bike(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = "bike"

    def __str__(self):
        return f"{self.name} - {self.company}"









