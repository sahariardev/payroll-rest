from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import renderers

from ..Models.salary_detail import SalaryDetail
from ..Serializers.salary_detail_serializer import SalaryDetailItemListSerializer



class SalaryCalculationTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):

        '''All data are avaialble on request.data
           get the data and then save one by one
        '''
        print(request.data)
        from_date=request.data.from_date
        till_date=request.data.till_date
        employee = request.data.employee
        print(from_date)
        print(till_date)
        print(employee)

        salary_details=SalaryDetail.objects.all().filter( effective_from__gte = from_date).filter(effective_till_date__lt=till_date).filter(employee__id=employee)
        serializer= SalaryDetailItemListSerializer(salary_details,many=True)
        return Response(serializer.data,tatus=status.HTTP_201_CREATED)