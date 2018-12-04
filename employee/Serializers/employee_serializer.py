from rest_framework.serializers import ModelSerializer
from ..Models.employee import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:


        #set the model
        model=Employee

        #set the fields list
        fields=['name','address','n_id','phone_number','email','pay_day','package_name','type_name'];
