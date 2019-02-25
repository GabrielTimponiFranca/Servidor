from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from Consulta.SGR.Consumo.TrafoA.models import hist_TrafoA, fun_raw_sql_query
from .serializers import trafoASerialiazer


class trafoAViewSet(ModelViewSet):
    queryset = hist_TrafoA.objects.using('dbGrandeRio').all()
    serializer_class = trafoASerialiazer

    #parser_classes = (JSONParser,)

    @action(methods=['get'], detail=False)
    def raw_sql_query(self, request, pk=None):
        hist = fun_raw_sql_query()
        serializer = trafoASerialiazer(hist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)