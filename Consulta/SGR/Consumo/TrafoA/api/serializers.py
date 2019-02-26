from rest_framework.serializers import ModelSerializer
from Consulta.SGR.Consumo.TrafoA.models import hist_TrafoA

class trafoASerialiazer(ModelSerializer):
    class Meta:
        model = hist_TrafoA
        #fields = ('Data', 'Consumo')
        fields = '__all__'
        