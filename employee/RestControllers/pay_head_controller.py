from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework import renderers
from ..Models.pay_head import  PayHead
from ..Serializers.pay_head_serializer import PayHeadCreateSerializer,PayHeadDetailSerializer,PayHeadListSerializer


class PayHeadListView(ListAPIView):
    queryset = PayHead.objects.all()
    serializer_class =PayHeadListSerializer
    renderer_classes = [renderers.JSONRenderer]


class PayHeadDetailView(RetrieveAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer
    renderer_classes = [renderers.JSONRenderer]


class PayHeadCreateView(CreateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadCreateSerializer



class PayHeadUpdateView(UpdateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer