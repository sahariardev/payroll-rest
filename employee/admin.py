from django.contrib import admin

from .Models.Package import Package
from .Models.Type import Type
from .Models.Employee import Employee
from .Models.Attendance import  Attendance
from .Models.bonus import Bonus
from .Models.GrantLeave import GrantLeave
from .Models.Advance import  Advance
from .Models.Payment import Payment
from .Models.Target import Target
from .Models.WorkedHours import WorkedHours

# Register your models here.
admin.site.register(Package)  # Salary Package
admin.site.register(Type)   # Employee Type
admin.site.register(Employee)   # Employee Entity
admin.site.register(Attendance)
admin.site.register(Bonus)
admin.site.register(GrantLeave)
admin.site.register(Advance)
admin.site.register(Payment)
admin.site.register(Target)
admin.site.register(WorkedHours)


