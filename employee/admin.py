from django.contrib import admin
from .models import Package,Type,Employee

# Register your models here.

admin.site.register(Package)
admin.site.register(Type)
admin.site.register(Employee)