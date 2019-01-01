from rest_framework.serializers import ModelSerializer,StringRelatedField
from ..Models.salary_detail_item import SalaryDetailItem
from ..Serializers.pay_head_serializer import PayHeadDetailSerializer



class SalaryDetailItemListSerializerWithPayHeadDetail(ModelSerializer):
    salary_detail = StringRelatedField()
    pay_head=PayHeadDetailSerializer()
    class Meta:
        model=SalaryDetailItem
        fields=['id','salary_detail','pay_head']

class SalaryDetailItemListSerializer(ModelSerializer):
    salary_detail = StringRelatedField()
    pay_head=StringRelatedField()
    class Meta:
        model=SalaryDetailItem
        fields=['id','salary_detail','pay_head']

class SalaryDetailItemDetailSerializer(ModelSerializer):
    salary_detail = StringRelatedField()
    pay_head = StringRelatedField()
    class Meta:
        model=SalaryDetailItem
        fields = ['id', 'salary_detail', 'pay_head','priority','value','rate','unit']
class SalaryDetailItemCreateSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetailItem
        fields = ['salary_detail', 'pay_head', 'priority', 'value', 'rate', 'unit']

