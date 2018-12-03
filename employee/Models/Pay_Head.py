from django.db import models

from .Employee import Employee
from .unit import Unit

class Pay_Head(models.Model):
    name = models.ForeignKey(Employee.name)
    add_net_salary = models.BooleanField()
    calculation_type = (('Flat Rate'),('On Attendence'),('On Production'),('As Computed Value'),('As Custom Value'));
    calculation_choice = models.CharField(choices=calculation_type)
    calculation_unit = models.ForeignKey(Unit.currency)