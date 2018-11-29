
from django.urls import path
from .RestControllers.employee_controller import EmployeeList
urlpatterns = [
    path('employees/',EmployeeList.as_view(), name="employees"),
]