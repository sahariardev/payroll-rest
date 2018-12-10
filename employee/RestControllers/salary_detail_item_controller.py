from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.salary_detail_item import SalaryDetailItem
from ..Serializers.salary_detail_item_serializer import  SalaryDetailItemListSerializer,SalaryDetailItemDetailSerializer,SalaryDetailItemCreateSerializer


class SalaryDetailItemListView(ListAPIView):
    queryset = SalaryDetailItem.objects.all()
    serializer_class = SalaryDetailItemListSerializer
    renderer_classes = [renderers.JSONRenderer]

class SalaryDetailItemDetailView(RetrieveAPIView):
    queryset = SalaryDetailItem.objects.all()
    lookup_field = 'pk'
    serializer_class = SalaryDetailItemDetailSerializer
    renderer_classes = [renderers.JSONRenderer]

class SalaryDetailItemUpdateView(UpdateAPIView):
    queryset = SalaryDetailItem.objects.all()
    lookup_field = 'pk'
    serializer_class = SalaryDetailItemDetailSerializer

class SalaryDetailItemCreateView(CreateAPIView):
    queryset = SalaryDetailItem.objects.all()
    serializer_class = SalaryDetailItemCreateSerializer