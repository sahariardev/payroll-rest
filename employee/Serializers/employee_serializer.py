from rest_framework.serializers import ModelSerializer
from ..Models.employee import Employee



class EmployeeSerializer(ModelSerializer):
    class Meta:
        #set the model
        model=Employee
        #set the fields list
        fields=['name','address','id'];
