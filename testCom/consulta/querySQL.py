import pandas as pd
from django.db import models, connection


class consulta(models.Manager):

    def ExecutarConsulta(self):
        # with connection['dbTeste'].cursor() as cursor:
            # sql = ('SELECT * FROM [Teste2]')
            # result = pd.read_sql_query(sql, connection)
            
        with connection.cursor() as cursor:
            try:
                cursor.execute('SELECT * FROM [Teste2]')
                result = []
                for row in cursor.fetchall(): 
                    p = self.model(TimeStamp=row[0], Teste01=row[1], Teste02=row[2])
                    result.append(p)
            finally:
                cursor.close() 

        return result
