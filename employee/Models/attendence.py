from django.db import models
from ..models import Employee

class Attendence(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField()
    arrival_time=models.TimeField()
    departure_time=models.TimeField()

    def __str__(self):
        return str(self.employee.name)+" Day :"+str(self.date)+" Arrival Time :"+self.arrival_time+" Departure Time:"+self.departure_time


