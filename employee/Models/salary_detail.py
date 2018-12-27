from django.db import models
from .employee import Employee


class SalaryDetail(models.Model):
    effective_from=models.DateField(blank=False)
    effective_till_date=models.DateField(blank=False)
    employee=models.ForeignKey(Employee,null=True, on_delete=models.SET_NULL,blank=False )
    name=models.CharField(max_length=30,null=True)

    def __str__(self):
        return "Salary detail of "+self.employee.name

    def __unicode__(self):
        return self.employee.name+" Effective from {a} Effective till date {b}".format(a=self.effective_from,b=self.effective_till_date)