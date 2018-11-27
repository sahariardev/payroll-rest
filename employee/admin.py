from django.contrib import admin

from employee.Models import Package, Type, Employee, Attendance, Bonus, GrantLeave

# Register your models here.
admin.site.register(Package)  # Salary Package
admin.site.register(Type)   # Employee Type
admin.site.register(Employee)   # Employee Entity
admin.site.register(Attendance)
admin.site.register(Bonus)
admin.site.register(GrantLeave)
