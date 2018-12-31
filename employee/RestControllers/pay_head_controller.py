from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
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
    #return the pk


class PayHeadTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):
        print("--------------------------")
        print(request.__getattr__('name'))
        print("--------------------------")
        print(request.POST.get('name'))
        print("--------------------------")
        return Response(request)




class PayHeadUpdateView(UpdateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer