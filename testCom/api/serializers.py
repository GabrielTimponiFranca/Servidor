from rest_framework.serializers import ModelSerializer
from testCom.models import testCom

class testComSerializer(ModelSerializer):
    class Meta:
        model = testCom
        fields = ('Teste01', 'Teste02')