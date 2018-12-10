from django.db import models
from .package import Package
from .designation import Designation


class Employee(models.Model):

    name=models.CharField(max_length=30,blank=False)
    date_of_joining=models.DateField(auto_now=True)
    #we do not want to delete any items from the db
    peckage=models.ForeignKey(Package,on_delete=models.SET_NULL, null=True)
    gender_choices=(('M','Male'),('F','Female'));
    gender=models.CharField(max_length=40, choices=gender_choices)
    date_of_birth=models.DateField()
    blood_group=models.CharField(max_length=30)
    marital_choices=(('Single','Single'),('Married','Married'))
    marital_status=models.CharField(max_length=40, choices=marital_choices)
    address=models.TextField()
    contact=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    spouse_name=models.CharField(max_length=30, blank=True)
    designation=models.ForeignKey(Designation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def __get__packageName(self):
        return self.peckage.name

    def __unicode__(self):
        return self.name
