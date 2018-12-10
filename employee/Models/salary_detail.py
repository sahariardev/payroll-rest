from django.db import models
from .employee import Employee


class SalaryDetail(models.Model):
    effective_from=models.DateField(blank=False)
    effective_till_date=models.DateField(blank=False)
    employee=models.ForeignKey(Employee,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Salary detail of "+self.employee.name
