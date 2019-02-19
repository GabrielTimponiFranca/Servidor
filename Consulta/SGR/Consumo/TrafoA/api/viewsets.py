from rest_framework.viewsets import ModelViewSet
from Consulta.SGR.Consumo.TrafoA.models import hist_TrafoA
from .serializers import trafoASerialiazer


class trafoAViewSet(ModelViewSet):
    queryset = hist_TrafoA.objects.all()
    serializer_class = trafoASerialiazer