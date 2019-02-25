import pandas as pd
from django.db import models

from django.db import connection
# Create your models here.

class hist_TrafoA(models.Model):
    E3TimeStamp = models.DateTimeField(db_column='E3TimeStamp', primary_key=True)
    #CorrenteA = models.FloatField(db_column='CorrenteA')
    Consumo = models.FloatField(db_column='Consumo', null=True, blank=True)
    # dataInicio = models.DateTimeField(null=True, blank=True)
    # DataFim = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hist_TrafoA'

    def __str__(self):
        return self.E3TimeStamp
