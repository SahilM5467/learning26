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

    












