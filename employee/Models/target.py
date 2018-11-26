from django.db import  models
from ..models import Employee

class Target(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    description=models.TextField(null=False)
    points=models.TextField(null=False)
    status=models.CharField(null=False)
