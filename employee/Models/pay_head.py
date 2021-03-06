from django.db import models

from .employee import Employee
from .unit import Unit
from .pay_head_type import  PayHeadType
from .production_attendance_type import  ProductionAttendanceType


class PayHead(models.Model):
    name=models.CharField(max_length=60,blank=False,null=True)
    description=models.TextField()
    add_net_salary = models.BooleanField()
    calculation_choices = (
                            ('Flat Rate','Flat Rate'),
                            ('On Attendence', 'On Attendence'),
                            ('On Production', 'On Production'),
                            ('As Computed Value', 'As Computed Value'),
                            ('As Custom Value', 'As Custom Value')
                          )
    rate=models.FloatField(null=True)
    rule = models.CharField(max_length=100, null=True)
    calculation_type = models.CharField(max_length=40, choices=calculation_choices)
    calculation_period = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    pay_head_type = models.ForeignKey(PayHeadType,on_delete=models.SET_NULL,null=True)
    attendence_production_type=models.ForeignKey(ProductionAttendanceType, null=True, on_delete=models.SET_NULL, blank=True)
    add_or_deduct=models.CharField(max_length=10,choices=(('add','add'),('deduct','deduct')),blank=False,null=False,default='add');
    under_types =((
                    'Direct Expense','Direct Expense'
                 ),
                 (
                     'Indirect Expense','Indirect Expense'
                 )
                 )
    under = models.CharField(max_length=40,choices=under_types)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
