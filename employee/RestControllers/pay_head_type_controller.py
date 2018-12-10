from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.pay_head_type import PayHeadType
from ..Serializers.pay_head_type_serializer import PayHeadTypeListSerializer,PayHeadTypeDetailSerializer,PayHeadTypeCreateSerializer

class PayHeadTypeListView(ListAPIView):
    queryset = PayHeadType.objects.all()
    serializer_class = PayHeadTypeListSerializer
    renderer_classes = [renderers.JSONRenderer]

class PayHeadTypeDetailView(RetrieveAPIView):
    queryset = PayHeadType.objects.all()
    serializer_class = PayHeadTypeDetailSerializer
    lookup_field = 'pk'
    renderer_classes = [renderers.JSONRenderer]

class PayHeadTypeCreateView(CreateAPIView):
    queryset = PayHeadType.objects.all()
    serializer_class = PayHeadTypeCreateSerializer

class PayHeadTypeUpdateView(UpdateAPIView):
    queryset = PayHeadType.objects.all()
    serializer_class = PayHeadTypeDetailSerializer