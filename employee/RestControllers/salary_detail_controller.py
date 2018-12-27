from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.salary_detail import SalaryDetail
from ..Serializers.salary_detail_serializer import SalaryDetailListSerializer,SalaryDetailDetailSerializer,SalaryDetailCreateSerializer,SalaryDetailUpdateSerializer


class SalaryDetailListView(ListAPIView):
    queryset = SalaryDetail.objects.all()
    serializer_class = SalaryDetailListSerializer
    renderer_classes = [renderers.JSONRenderer]

class SalaryDetailDetailView(RetrieveAPIView):
    queryset = SalaryDetail.objects.all()
    lookup_field = 'pk'
    serializer_class = SalaryDetailDetailSerializer
    renderer_classes = [renderers.JSONRenderer]

class SalaryDetailUpdateView(UpdateAPIView):
    queryset = SalaryDetail.objects.all()
    lookup_field = 'pk'
    serializer_class = SalaryDetailUpdateSerializer

class SalaryDetailCreateView(CreateAPIView):
    queryset = SalaryDetail.objects.all()
    serializer_class = SalaryDetailCreateSerializer
