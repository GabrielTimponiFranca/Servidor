from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

from testCom.api.serializers import testComSerializer
from .consulta.querySQL import *

consulta = consulta()

# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def raw_sql_query(request):

    if request.method == 'GET':
        hist = consulta.ExecutarConsulta()
        serializer = testComSerializer(hist, many=True)
        return JsonResponse(serializer.data, safe=False)