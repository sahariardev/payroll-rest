from django.db import models
from .salary_detail import SalaryDetail
from .pay_head import  PayHead
from .unit import Unit


class SalaryDetailItem(models.Model):
    salary_detail=models.ForeignKey(SalaryDetail, on_delete=models.SET_NULL)
    priority=models.IntegerField(default=0)
    pay_head=models.ForeignKey(PayHead, on_delete=models.SET_NULL)
    value=models.FloatField(blank=False)
    rate=models.FloatField(blank=False)
    unit=models.ForeignKey(Unit, blank=False,on_delete=models.SET_NULL)

    def __str__(self):
        return "Salary Detail Items : "+self.salary_detail.employee.name
