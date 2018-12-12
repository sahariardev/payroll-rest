from django.conf.urls import url




from .RestControllers.pay_head_type_controller import PayHeadTypeListView, PayHeadTypeDetailView, PayHeadTypeCreateView,\
    PayHeadTypeUpdateView
from .RestControllers.attendance_controller import AttendanceListView, AttendanceDetailView,\
    AttendanceCreateView, AttendanceUpdateView,EmplyeeAttendanceListView,EmplyeeAttendanceInDateRangeListView
from .RestControllers.employee_controller import EmployeeList,EmployeeDetail,EmployeeCreate,EmployeeUpdate
from .RestControllers.unit_controller import  UnitListView,UnitDetailView,UnitCreateView,UnitUpdateView
from .RestControllers.package_controller import  PackageListView,PackageDetailView,PackageCreateView,PackageUpdateView
from .RestControllers.pay_head_controller import PayHeadListView,PayHeadCreateView,PayHeadDetailView,PayHeadUpdateView
from .RestControllers.salary_detail_controller import SalaryDetailListView,SalaryDetailDetailView,SalaryDetailUpdateView,SalaryDetailCreateView
from .RestControllers.salary_detail_item_controller import SalaryDetailItemListView,SalaryDetailItemDetailView, SalaryDetailItemUpdateView,SalaryDetailItemCreateView
from .RestControllers.production_attendance_type_controller import ProductionAttendanceTypeListView,ProductionAttendanceTypeDetailView, ProductionAttendanceTypeUpdateView,ProductionAttendanceTypeCreateView
from .RestControllers.computation_info_controller  import ComputationInfoListView,ComputationInfoDetailView,ComputationInfoUpdateView,ComputationInfoCreateView


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
    url(r'^packages/(?P<pk>\d+)/edit/$', PackageUpdateView.as_view(), name="package_update"),


    url("payheadtypes/$",PayHeadTypeListView.as_view(),name="payheadtypes"),
    url(r'^payheadtypes/(?P<pk>\d+)/$',PayHeadTypeDetailView.as_view(), name="payheadtype"),
    url(r'^packages/create/$', PayHeadTypeCreateView.as_view(), name="payheadtypes_create"),
    url(r'^packages/(?P<pk>\d+)/edit/$', PayHeadTypeUpdateView.as_view(), name="package_update"),

    url(r"^attendances/$",AttendanceListView.as_view(),name="attendances"),
    url(r'^attendances/(?P<pk>\d+)/$',AttendanceDetailView.as_view(), name="attendance"),
    url(r'^attendances/create/$', AttendanceCreateView.as_view(), name="attendance_create"),
    url(r'^attendances/(?P<pk>\d+)/edit/$', AttendanceUpdateView.as_view(), name="attendance_update"),
    url(r"^employees/(?P<employee_id>\d+)/attendances/$",EmplyeeAttendanceListView.as_view(),name="employee_attendance"),
    url(r"^employees/(?P<employee_id>\d+)/attendances/fromdate/(?P<from_date>\d{4}-\d{2}-\d{2})/tilldate/(?P<till_date>\d{4}-\d{2}-\d{2})/$",EmplyeeAttendanceInDateRangeListView.as_view(),name="employee_attendance_in_date_range"),



    url("payheads/$", PayHeadListView.as_view(), name="payheads"),
    url(r'^payheads/(?P<pk>\d+)/$', PayHeadDetailView.as_view(), name="payhead"),
    url(r'^payheads/create/$', PayHeadCreateView.as_view(), name="payhead_create"),
    url(r'^payheads/(?P<pk>\d+)/edit/$', PayHeadUpdateView.as_view(), name="payhead_update"),

    url("salarydetails/$", SalaryDetailListView.as_view(), name="salarydetails"),
    url(r'^salarydetails/(?P<pk>\d+)/$', SalaryDetailDetailView.as_view(), name="salarydetails"),
    url(r'^salarydetails/create/$', SalaryDetailCreateView.as_view(), name="salarydetails_create"),
    url(r'^salarydetails/(?P<pk>\d+)/edit/$', SalaryDetailUpdateView.as_view(), name="salarydetails_update"),

    url("salarydetailitems/$", SalaryDetailItemListView.as_view(), name="salarydetails"),
    url(r'^salarydetailitems/(?P<pk>\d+)/$', SalaryDetailItemDetailView.as_view(), name="salarydetails"),
    url(r'^salarydetailitems/create/$', SalaryDetailItemCreateView.as_view(), name="salarydetails_create"),
    url(r'^salarydetailitems/(?P<pk>\d+)/edit/$', SalaryDetailItemUpdateView.as_view(), name="salarydetails_update"),

    url("productionattendencetypes/$", ProductionAttendanceTypeListView.as_view(), name="productionattendencetypes"),
    url(r'^productionattendencetypes/(?P<pk>\d+)/$', ProductionAttendanceTypeDetailView.as_view(), name="productionattendencetypes"),
    url(r'^productionattendencetypes/create/$', ProductionAttendanceTypeCreateView.as_view(), name="productionattendencetypes_create"),
    url(r'^productionattendencetypes/(?P<pk>\d+)/edit/$', ProductionAttendanceTypeUpdateView.as_view(), name="productionattendencetypes_update"),

    url(r"^computationinfos/$", ComputationInfoListView.as_view(), name="computationinfos"),
    url(r'^computationinfos/(?P<pk>\d+)/$', ComputationInfoDetailView.as_view(), name="computationinfo"),
    url(r'^computationinfos/create/$', ComputationInfoCreateView.as_view(), name="computationinfos_create"),
    url(r'^computationinfos/(?P<pk>\d+)/edit/$', ComputationInfoUpdateView.as_view(), name="computationinfos_update")


]


