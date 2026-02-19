from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "services"

    def __str__(self):
        return self.serviceName    