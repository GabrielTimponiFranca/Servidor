from django.db import models

# Create your models here.


class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""\
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
                FROM GrandeRio.dbo.hist_TrafoA   
                ORDER BY hist_TrafoA.E3TimeStamp ASC     
            """)
            result_list = []

            return result_list

class hist_TrafoA(models.Model):
    E3TimeStamp = models.DateTimeField()
    CorrenteA = models.FloatField()
    #objects = PollManager()

    
    #class Meta:
    #    db_table = '[GrandeRio].[dbo].[hist_TrafoA]'

    def __str__(self):
        return self.E3TimeStamp
