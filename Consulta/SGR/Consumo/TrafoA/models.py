from django.db import models


class hist_TrafoA(models.Model):
    Data = models.DateTimeField(db_column='E3TimeStamp', primary_key=True)
    Consumo = models.FloatField(db_column='Consumo', null=True, blank=True)
    CorrenteA = models.FloatField(db_column='CorrenteA', null=True, blank=True)
    CorrenteB = models.FloatField(db_column='CorrenteB', null=True, blank=True)
    CorrenteC = models.FloatField(db_column='CorrenteC', null=True, blank=True)
    # dataInicio = models.DateTimeField(null=True, blank=True)
    # DataFim = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hist_TrafoA'

    def __str__(self):
        return self.Data
