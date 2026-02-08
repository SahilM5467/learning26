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
    categoryId = models.ForeignKey(Category,default=True, on_delete=models.CASCADE)
    serviceName = models.CharField(max_length=100)
    serviceDesccription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "service"
    
    def __str__(self):
        return self.serviceName

# ---------------------------------------------------------------------------------------------

# Task : Bank Management System
# 2 tables : 1 - 1 relationship ( OneToOneField )
# 4 tables : 1 - M relationship ( ForeignKey )


class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    customerPhone = models.CharField(max_length=10)

    class Meta :
        db_table = "customer"

    def __str__(self):
        return self.customerName

class customerProfile(models.Model):
    gender = ( ("Male","Male"), ("Female","Female"), ("Other","Other") )

    customerId = models.OneToOneField(Customer, on_delete=models.CASCADE) 
    customerGender = models.CharField(max_length=10, choices=gender)
    customerDOB = models.DateField()
    customerAddress = models.TextField()
    customerCity = models.CharField(max_length=25)
    customerState = models.CharField(max_length=25)
    customerPincode = models.CharField(max_length=6) 

    class Meta :
        db_table = "customerProfile"

    def __str__(self):
        return self.customerId.customerName

class Account(models.Model):
    account_type = ( ("Current","Current"), ("Savings","Savings") )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    accountNumber = models.CharField(max_length=50, unique=True)
    accountType = models.CharField(max_length=50, choices=account_type)
    accountBalance = models.DecimalField(max_digits=10, decimal_places=2)
    accountStatus = models.BooleanField(default=True)
    
    class Meta :
        db_table = "account"

    def __str__(self):
        return f" {self.accountNumber} - {self.customer.customerName} "

class Transaction(models.Model):
    transaction_type = ( ("Deposit","Deposit"), ("Withdraw","Withdraw"), ("Transfer","Transfer") )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transactionType = models.CharField(max_length=50, choices=transaction_type)
    transactionAmount = models.DecimalField(max_digits=10, decimal_places=2)
    transactionDate = models.DateField(auto_now_add=True)

    class Meta :
        db_table = "transaction"

    def __str__(self):
        return f" {self.account.accountNumber} - {self.transactionType} - {self.transactionAmount} "
    
class Loan(models.Model):
    loan_type = ( ("Home Loan","Home Loan"), ("Education Loan","Education Loan"), ("Personal Loan","Personal Loan") )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loanType = models.CharField(max_length=25, choices=loan_type) 
    loanAmount = models.DecimalField(max_digits=10, decimal_places=2)
    loanIntrestRate = models.DecimalField(max_digits=5, decimal_places=2)
    loanStatus = models.BooleanField(default=True)
    
    class Meta :
        db_table = "loan"

    def __str__(self):
        return f" {self.loanType} - {self.customer.customerName} "
    
class Card(models.Model):
    card_type = ( ("Debit Card","Debit Card"), ("Credit Card","Credit Card") )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=16, unique=True)
    cardType = models.CharField(max_length=25, choices=card_type)
    cardExpiryDate = models.DateField()
    cardStatus = models.BooleanField(default=True)

    class Meta :
        db_table = "card"

    def __str__(self):
        return f" {self.account.accountNumber} - {self.cardType} - {self.cardNumber} "
















