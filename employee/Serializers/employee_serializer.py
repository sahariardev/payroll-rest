from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField
from ..Models.employee import Employee



class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields=['name','address','id','date_of_joining','email']

class EmployeeDetailSerializer(ModelSerializer):
    peckage=StringRelatedField()
    designation=StringRelatedField()
    class Meta:
        #set the model
        model=Employee
        #set the fields list
        fields=['name','address','id','date_of_joining','gender','date_of_birth','blood_group','marital_status','address','contact','email','spouse_name','designation','peckage']

class EmployeeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        #set the model
        model=Employee
        #set the fields list
        fields=['name','address','date_of_joining','gender','date_of_birth','blood_group','marital_status','address','contact','email','spouse_name','designation','peckage']