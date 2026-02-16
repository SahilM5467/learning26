from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = "services"

    def __str__(self):
        return f"{self.name} - {self.category}"