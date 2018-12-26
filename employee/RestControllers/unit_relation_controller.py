from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.unit_relation import UnitRelation
from ..Serializers.unit_relation_serializer import UnitRelationListSerializer,UnitRelationDetailSerializer,UnitRelationCreateSerializer


class UnitRelationListView(ListAPIView):
    queryset = UnitRelation.objects.all()
    serializer_class = UnitRelationListSerializer
    renderer_classes = [renderers.JSONRenderer]

class UnitRelationDetailView(RetrieveAPIView):
    queryset = UnitRelation.objects.all()
    lookup_field = 'pk'
    serializer_class = UnitRelationDetailSerializer
    renderer_classes = [renderers.JSONRenderer]

class UnitRelationUpdateView(UpdateAPIView):
    queryset = UnitRelation.objects.all()
    lookup_field = 'pk'
    serializer_class = UnitRelationDetailSerializer

class UnitRelationCreateView(CreateAPIView):
    queryset = UnitRelation.objects.all()
    serializer_class = UnitRelationCreateSerializer