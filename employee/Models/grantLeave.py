from django.db import models
from ..models import Employee

class GrantLeave(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField(null=False)
    extra=models.TextField(null=True)
