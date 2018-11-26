from django.db import models
from ..models import Employee

class GrantLeave(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    from_date = models.DateField(null=False)
    to_date=models.DateField(null=False)
    cause = models.TextField(null=False)
    extra=models.TextField(null=True)


    def __str__(self):
        return self.employee.name+" "+self.date