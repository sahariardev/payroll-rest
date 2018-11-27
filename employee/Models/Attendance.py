from django.db import models

from .Employee import Employee


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return str(self.employee.name) + " Day :" + str(
            self.date) + " Arrival Time :" + str(self.arrival_time) + " Departure Time:" + str(self.departure_time)
