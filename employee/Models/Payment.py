from django.db import models
from ..models import Employee

class Payment(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    amount=models.IntegerField(null=False)
    amount_type=models.CharField(null=False)
    date=models.DateField()


    def __str__(self):
        return self.employee.name+" Date "+self.date+" Amount "+self.amount+"Amount Type "+self.amount_type

