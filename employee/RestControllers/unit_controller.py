from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.unit import Unit
from ..Serializers.unit_serializer import UnitListSerializer,UnitDetailSerializer,UnitCreateSerializer


class UnitListView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitListSerializer
    renderer_classes = [renderers.JSONRenderer]


class UnitDetailView(RetrieveAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitDetailSerializer
    lookup_field = 'pk'
    renderer_classes = [renderers.JSONRenderer]


class UnitCreateView(CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitCreateSerializer


class UnitUpdateView(UpdateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitDetailSerializer