from rest_framework.serializers import ModelSerializer,StringRelatedField
from ..Models.salary_detail import SalaryDetail

class SalaryDetailListSerializer(ModelSerializer):
    employee = StringRelatedField()
    class Meta:
        model=SalaryDetail
        fields=['id','effective_from','effective_till_date','employee'];

class SalaryDetailDetailSerializer(ModelSerializer):
    employee = StringRelatedField()
    class Meta:
        model=SalaryDetail
        fields = ['id', 'effective_from', 'effective_till_date', 'employee'];

class SalaryDetailCreateSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        fields = ['effective_from', 'effective_till_date', 'employee'];

