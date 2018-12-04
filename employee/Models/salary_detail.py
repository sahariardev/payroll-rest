from django.db import models
from .employee import Employee


class SalaryDetail(models.Model):
    effective_from=models.DateField(blank=False)
    effective_till_date=models.DateField(blank=False)
    employee=models.ForeignKey(Employee, on_delete=models.SET_NULL)

