from django.db import models

from .employee import Employee
from .unit import Unit
from .pay_head_type import  PayHeadType


class PayHead(models.Model):

    name = models.ForeignKey(Employee.name)
    description=models.TextField()
    add_net_salary = models.BooleanField()
    calculation_choices = (
                            ('Flat Rate'),
                            ('On Attendence'),
                            ('On Production'),
                            ('As Computed Value'),
                            ('As Custom Value')
                          )
    calculation_type = models.CharField(choices=calculation_choices)
    calculation_unit = models.ForeignKey(Unit.currency,on_delete=models.SET_NULL)
    pay_head_type=models.ForeignKey(PayHeadType,on_delete=models.Set_NULL)
    under_types=((
                    'Direct Expense'
                 ),
                 (
                     'Indirect Expense'
                 )
                 )
    under=models.CharField(choices=under_types)

    def __str__(self):
        return self.name


