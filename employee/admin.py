from django.contrib import admin
from .models import Package,Type,Employee,Bonus

# Register your models here.

admin.site.register(Package)
admin.site.register(Type)
admin.site.register(Employee)
admin.site.register(Bonus)