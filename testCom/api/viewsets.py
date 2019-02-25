from rest_framework.viewsets import ModelViewSet
from testCom.models import testCom
from .serializers import testComSerializer


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

from testCom.consulta.querySQL import *

consulta = consulta()

class testComViewSet(ModelViewSet):
    #queryset = testCom.objects.using('dbTeste').all()
    queryset = testCom.objects.using('dbTeste').all()
    serializer_class = testComSerializer
