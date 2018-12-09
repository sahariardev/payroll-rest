from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import  renderers
from ..Models.unit import Unit
from ..Serializers.unit_serializer import UnitListSerializer

class UnitListView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitListSerializer
    renderer_classes = [renderers.JSONRenderer]