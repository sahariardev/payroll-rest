from django.db import models
from .pay_head import PayHead


class ComputationInfo(models.Model):

    pay_head = models.ForeignKey(PayHead, on_delete=models.SET_NULL , null=True)
    effective_from=models.DateField(blank=False)
    effective_till_date=models.DateField(blank=False)
    rule=models.CharField(max_length=40,null=False,blank=False)
    name=models.CharField(max_length=30,null=False,blank=False)


    def __str__(self):

        return self.name

