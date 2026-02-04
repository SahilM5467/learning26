from django.db import models

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=100)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productStock = models.PositiveIntegerField()
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseType = models.CharField(max_length=100)
    coursePrice = models.IntegerField()
    courseDays = models.IntegerField(null=True)
    courseStatus = models.BooleanField(null=True)

    class Meta:
        db_table = "course"







