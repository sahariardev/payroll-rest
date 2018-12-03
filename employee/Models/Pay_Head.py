from django.db import models

from .Employee import Employee
from .unit import Unit

class Pay_Head(models.Model):
    name = models.ForeignKey(Employee.name)
    add_net_salary = models.BooleanField()
    calculation_choices = (('Flat Rate'),('On Attendence'),('On Production'),('As Computed Value'),('As Custom Value'));
    calculation_type = models.CharField(choices=calculation_choices)
    calculation_unit = models.ForeignKey(Unit.currency,on_delete=models.SET_NULL)