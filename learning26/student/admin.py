from django.contrib import admin
from . models import Student,Product,Course,StudentProfile,Category,Service
from . models import Customer, customerProfile, Account, Transaction, Loan, Card

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)

admin.site.register(Customer)
admin.site.register(customerProfile)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Loan)
admin.site.register(Card)