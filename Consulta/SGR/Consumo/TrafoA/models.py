import pandas as pd
from django.db import models
from collections import namedtuple

from django.db import connection
# Create your models here.

class PollManager(models.Manager):
    def with_counts(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT E3TimeStamp AS Data, 
                    CorrenteA AS [CorA], 
                    TensaoA AS [TA], 
                    CorrenteB AS [CorB], 
                    TensaoB AS [TB], 
                    CorrenteC AS [CorC], 
                    TensaoC AS [TC],
                    PotenciaA AS [PotA],
                    PotenciaB AS [PotB],
                    PotenciaC AS [PotC],
                    Potencia AS [Pot],
                    FPA,
                    FPB,
                    FPC,
                    FPTotal AS [FP]
                FROM hist_TrafoA   
                ORDER BY hist_TrafoA.E3TimeStamp ASC     
            """)
            result = cursor.fetchall()

            return result

class hist_TrafoA(models.Model):
    E3TimeStamp = models.DateTimeField()
    CorrenteA = models.FloatField()
    #objects = PollManager()

    class Meta:
        #db_table = '[GrandeRio].[dbo].[hist_TrafoA]'
        db_table = 'hist_TrafoA'

    def __str__(self):
        return self.E3TimeStamp


def fun_raw_sql_query(self):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM hist_TrafoA ORDER BY hist_TrafoA.E3TimeStamp ASC')
        result = cursor.fetchall()
    
    #result = hist_TrafoA.objects.raw('SELECT * FROM hist_TrafoA ORDER BY hist_TrafoA.E3TimeStamp ASC')

    
    #connection.cursor() 
    #sql = ('SELECT * FROM hist_TrafoA ORDER BY hist_TrafoA.E3TimeStamp ASC')
    #result = pd.read_sql_query(sql, connection)
    return result
