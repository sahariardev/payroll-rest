
from django.db import models
from .employee import Employee
from .production_attendence_type import ProductionAttendenceType
from .unit import Unit

'''Attendance or production'''


class Attendance(models.Model):
    employee = models.ForeignKey(Employee,null=True, on_delete=models.SET_NULL,blank=False)
    production_attendance_type=models.ForeignKey(ProductionAttendenceType, null=True, on_delete=models.SET_NULL,blank=False)
    value=models.FloatField(blank=False,null=False,default=0)
    unit=models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    date=models.DateField(null=True);

    def __str__(self):
        return "Attendance of  "+self.employee.name