from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from testCom.models import testCom
from .serializers import testComSerializer


class testComViewSet(ModelViewSet):
    #queryset = testCom.objects.using('dbTeste').all()
    # queryset = testCom.objects.all()
    queryset = testCom.objects.using('dbTeste').all()
    serializer_class = testComSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = testComSerializer(list(queryset), many=True)
        return Response(serializer.data)
