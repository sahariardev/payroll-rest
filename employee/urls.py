
from django.urls import path
from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary,EmployeeDetail,EmployeeCreate,EmployeeUpdate

urlpatterns = [

    url("employees/$",EmployeeList.as_view(),name="employees"),
    url(r'^employees/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name="employee"),
    url(r'^employees/create/$',EmployeeCreate.as_view(),name="create"),
    url(r'^employees/(?P<pk>\d+)/edit/$',EmployeeUpdate.as_view(),name="update")
]