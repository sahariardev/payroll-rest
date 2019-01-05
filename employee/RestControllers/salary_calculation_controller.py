from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import renderers

from ..Models.salary_detail import SalaryDetail
from ..Serializers.salary_detail_serializer import SalaryDetailListSerializer
from  ..Models.attendance import Attendance
from ..Serializers.attendance_serializer import AttendanceSerializerForSalaryCalculation
import  re
from ..Service.expression_evaluation import ExpressionEvaluation


class SalaryCalculationTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):

        '''All data are avaialble on request.data
           get the data and then save one by one
        '''

        evaluate_expression=ExpressionEvaluation()
        from_date=request.data.get('from_date')
        till_date=request.data['till_date']
        employee = request.data['employee']
        datamap={}


        print(employee)

        salary_details=SalaryDetail.objects.all().filter( effective_from__gte = from_date).filter(employee__id=employee)
        #salary_details = SalaryDetail.objects.all().filter(employee__id=employee)
        serializer= SalaryDetailListSerializer(salary_details,many=True)
        print(serializer.data)
        salary_detail_items=serializer.data[0]['salary_detail_item']

        for salary_detail_item in salary_detail_items:
            pay_head=salary_detail_item['pay_head']
            dbc=""
            sign="+"
            if(pay_head['add_or_deduct']=='add'):
                dbc="Credited"
                sign="+"
            else:
                dbc="Debited"
                sign="-"

            if((pay_head['calculation_type'] =='On Production') or (pay_head['calculation_type'] =='On Attendence')):
                #find the attendances where date in range and employee and attendance ids are same

                attendance_id=pay_head['attendence_production_type']
                attendances=Attendance.objects.all().filter(employee__id=employee).filter(production_attendance_type__id=attendance_id).filter(date__gte=from_date).filter(date__lte=till_date)
                attendance_data_serializer=AttendanceSerializerForSalaryCalculation(attendances,many=True)


                sum=0
                if(len(attendance_data_serializer.data) !=0):
                    for v in attendance_data_serializer.data:
                        print(v)
                        print(v['value'])
                        sum = sum + v['value']



                    final_amount = salary_detail_item['value'] * sum / salary_detail_item['rate']
                    print("---------------------------------------")
                    print(pay_head['description'])
                    print(dbc+" for {a} {b}".format(a=sum,b=salary_detail_item['unit']['name']))
                    print(final_amount)
                    print("---------------------------------------")
                    pay_head_id=pay_head['id']
                    datamap[pay_head_id]={
                        'description':pay_head['description'],
                        'detail':dbc+" for {a} {b}".format(a=sum,b=salary_detail_item['unit']['name']),
                        'amount':final_amount,
                        'sign':sign
                    }
                    print(datamap)

            elif(pay_head['calculation_type'].lower()=='As Computed Value'.lower()):
                tokens=pay_head['rule'].split()
                tokensforeval=[]
                for token in tokens:
                    if(re.search(r"^ID-\d",token)):
                       dependent_pay_head_id=token.split("-")[1]
                       value=datamap[int(dependent_pay_head_id)].amount
                       tokensforeval.append(value)

                    else:
                        tokensforeval.append(token)

                final_amount=evaluate_expression.evaluate(tokensforeval)
                pay_head_id = pay_head['id']
                datamap[pay_head_id]={
                    'description': pay_head['description'],
                    'detail':dbc,
                    'amount': final_amount,
                    'sign':sign
                }



        print(datamap)
        return Response(serializer.data,status=status.HTTP_201_CREATED)