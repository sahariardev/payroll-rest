from django.db import models

# Create your models here.
#Package model
class Package(models.Model):
    name=models.CharField(max_length=30)
    annual_leave=models.IntegerField()
    sick_leave=models.IntegerField()
    extra=models.TextField()
    description=models.TextField()

    def __str__(self):
        return self.name

#Type Model
class Type(models.Model):
    type=models.CharField(max_length=30,unique=True)
    description=models.TextField(null=False)

    def __str__(self):
        return self.type

#model employees
class Employee(models.Model):
    name=models.CharField(max_length=30,null=False)
    address=models.TextField(null=False)

