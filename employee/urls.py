
from django.urls import path
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary

urlpatterns = [

    path("employees/",EmployeeList.as_view(),name="employees"),
    path("employee/(?P<pk>\d+)/$",EmployeeSalary.as_view(),name="employee")
]