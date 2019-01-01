from rest_framework.serializers import ModelSerializer,StringRelatedField,SerializerMethodField
from .salary_detail_item_serializer import  SalaryDetailItemListSerializer,SalaryDetailItemDetailSerializer,SalaryDetailItemListSerializerWithPayHeadDetail
from ..Models.salary_detail import SalaryDetail
from ..Models.salary_detail_item import SalaryDetailItem

class SalaryDetailListSerializer(ModelSerializer):
    employee = StringRelatedField()
    salary_detail_item=SerializerMethodField()

    def get_salary_detail_item(self,obj):
        salary_details_items_data=SalaryDetailItem.objects.filter(salary_detail_id=obj.id)
        d=SalaryDetailItemListSerializerWithPayHeadDetail(salary_details_items_data, many=True)
        return d.data
    class Meta:
        model=SalaryDetail
        fields=['id','effective_from','name','effective_till_date','employee','salary_detail_item'];

class SalaryDetailDetailSerializer(ModelSerializer):
    employee = StringRelatedField()
    salary_detail_item = SerializerMethodField()

    def get_salary_detail_item(self, obj):
        salary_details_items_data = SalaryDetailItem.objects.filter(salary_detail_id=obj.id)
        d = SalaryDetailItemDetailSerializer(salary_details_items_data, many=True)
        return d.data
    class Meta:
        model=SalaryDetail
        fields = ['id', 'effective_from','name', 'effective_till_date', 'employee','salary_detail_item'];

class SalaryDetailCreateSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        fields = ['effective_from', 'name','effective_till_date', 'employee'];

class SalaryDetailUpdateSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        fields = ['id','effective_from', 'effective_till_date',];

