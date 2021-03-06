
from django.db import models
from .salary_detail import SalaryDetail
from .pay_head import  PayHead
from .unit import Unit


class SalaryDetailItem(models.Model):
    salary_detail=models.ForeignKey(SalaryDetail, null=True, on_delete=models.SET_NULL)
    priority=models.IntegerField(default=0)
    pay_head=models.ForeignKey(PayHead, on_delete=models.SET_NULL,null=True)
    value=models.FloatField(blank=False,null=True)
    rate=models.FloatField(blank=False,null=True)
    unit=models.ForeignKey(Unit, blank=False,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return "Salary Detail Items : "+self.salary_detail.employee.name