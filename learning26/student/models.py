from django.db import models

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=100)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student"
    
    def __str__(self):
        return self.studentName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productStock = models.PositiveIntegerField()
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"
    
    def __str__(self):
        return self.productName


class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseType = models.CharField(max_length=100)
    coursePrice = models.IntegerField()
    courseDays = models.IntegerField(null=True)
    courseStatus = models.BooleanField(null=True)

    class Meta:
        db_table = "course"
    
    def __str__(self):
        return self.courseName

class StudentProfile(models.Model):
    hobbies = (("Reading","Reading"),("Travel","Travel"),("Music","Music"))

    studentId = models.OneToOneField(Student, on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100, choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table = "studentProfile"
    
    def __str__(self):
        return self.studentId.studentName

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.categoryName

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDesccription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    categoryId = models.ForeignKey(Category,default=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "service"
    
    def __str__(self):
        return self.serviceName



























