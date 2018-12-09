from rest_framework.serializers import ModelSerializer
from ..Models.unit import Unit


class UnitListSerializer(ModelSerializer):
    class Meta:
        model=Unit
        fields=['name','symbol'];


'''This serializer will be used for detail, create and update'''


class UnitDetailSerializer(ModelSerializer):
    class Meta:
        model=Unit
        fields=['name','symbol','description'];


