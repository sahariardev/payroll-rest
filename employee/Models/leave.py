from django.db import models
from ..models import Employee

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    duration = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    cause = models.TextField(null=False)


    def __str__(self):
        return str(self.employee.name)+" Day :"+str(self.duration)+" From :"+self.from_date+" To :"+self.to_date+" Cause :"+self.cause