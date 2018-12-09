

from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework import  renderers
from ..Models.employee import Employee
from rest_framework.views import APIView
from ..Serializers.employee_serializer import EmployeeSerializer,EmployeeCreateSerializer
from ..Service.salary_calculate_service import SalaryCalculateService
from rest_framework.response import Response

'''All Employee Listview '''
class EmployeeList(ListAPIView):
    #model added and data fetched
    employees=Employee.objects.all()
    #serializer added
    serializer_class = EmployeeSerializer
    #show raw josn
    renderer_classes = [renderers.JSONRenderer]
    def get_queryset(self):
        return self.employees

'''One Employee Detail View'''
class EmployeeDetail(RetrieveAPIView):
    # model added and data fetched
    employees = Employee.objects.all()
    # serializer added
    serializer_class = EmployeeSerializer
    # show raw josn
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        return self.employees

'''One Employee Create View'''
class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer





class EmployeeSalary(APIView):

    employee=Employee.objects.get(pk=1)
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print(employee)
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")
    print("-------------------------------")

    renderer_classes = [renderers.JSONRenderer]
    def get_queryset(self):
        return self.employee
    def get(self, request,pk):
        s=EmployeeSerializer(self.employee)
        return Response(data={"status":s.data})





