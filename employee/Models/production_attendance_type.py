from  django.db import  models


class ProductionAttendanceType(models.Model):
    name=models.CharField(max_length=30,blank=False)
    type_choices=(
        ('Production','Production'),
        ('attendance/leave with pay', 'attendance/leave with pay'),
        ('attendance/leave without pay', 'attendance/leave without pay')
    )
    type=models.CharField(max_length=30,choices=type_choices)

    def __str__(self):
        return self.name