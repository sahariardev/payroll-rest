
from django.urls import path
from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary,EmployeeDetail,EmployeeCreate,EmployeeUpdate
from .RestControllers.unit_controller import  UnitListView,UnitDetailView,UnitCreateView,UnitUpdateView
from .RestControllers.package_controller import  PackageListView,PackageDetailView,PackageCreateView,PackageUpdateView

urlpatterns = [

    url("employees/$",EmployeeList.as_view(),name="employees"),
    url(r'^employees/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name="employee"),
    url(r'^employees/create/$',EmployeeCreate.as_view(),name="create"),
    url(r'^employees/(?P<pk>\d+)/edit/$',EmployeeUpdate.as_view(),name="update"),

    url("units/$", UnitListView.as_view(), name="units"),
    url(r'^units/(?P<pk>\d+)/$', UnitDetailView.as_view(), name="unit"),
    url(r'^units/create/$', UnitCreateView.as_view(), name="unit_create"),
    url(r'^units/(?P<pk>\d+)/edit/$', UnitUpdateView.as_view(), name="unit_update"),

    url("packages/$",PackageListView.as_view(),name="packages"),
    url(r'^packages/(?P<pk>\d+)/$',PackageDetailView.as_view(), name="package"),
    url(r'^packages/create/$', PackageCreateView.as_view(), name="package_create"),
    url(r'^packages/(?P<pk>\d+)/edit/$', PackageUpdateView.as_view(), name="package_update")
]

