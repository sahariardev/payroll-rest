from rest_framework.serializers import ModelSerializer
from ..Models.unit_relation import UnitRelation


class UnitRelationListSerializer(ModelSerializer):
    class Meta:
        model=UnitRelation
        fields=['id','value','first_unit','second_unit']
class UnitRelationDetailSerializer(ModelSerializer):
    class Meta:
        model=UnitRelation
        fields=['id','value','first_unit','second_unit','effective_from','effective_till_date']

class UnitRelationCreateSerializer(ModelSerializer):
    class Meta:
        model=UnitRelation
        fields=['value','first_unit','second_unit','effective_from','effective_till_date']
