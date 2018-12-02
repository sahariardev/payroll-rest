
'''
from rest_framework.generics import ListAPIView
from ..Models.Employee import Employee
from ..Serializers.employee_serializer import EmployeeSerializer


class EmployeeList(ListAPIView):

        TO create a List view api we need to extend ListAPIView from
       rest_frameworks.generics then get all data using model
       after that add the serializer


    #model added and data fetched
    employees=Employee.objects.all()

    #serializer added
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return self.employees

'''


