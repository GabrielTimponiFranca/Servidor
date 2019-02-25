from django.db.models.functions import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from Consulta.SGR.Consumo.TrafoA.models import hist_TrafoA#, fun_raw_sql_query
from .serializers import trafoASerialiazer


class trafoAViewSet(ModelViewSet):
    queryset = hist_TrafoA.objects.using('dbGrandeRio').all()
    serializer_class = trafoASerialiazer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = trafoASerialiazer(list(queryset), many=True)
        return Response(serializer.data)
