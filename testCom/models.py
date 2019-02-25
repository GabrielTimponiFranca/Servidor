from django.db import models

# Create your models here.

class testCom(models.Model):
    TimeStamp = models.DateTimeField(db_column='TimeStamp', primary_key=True)
    Teste01 = models.FloatField(db_column='Teste01')
    Teste02 = models.FloatField(db_column='Teste02')

    class Meta:       
        db_table = 'Teste2'

    def __str__(self):
        return self.TimeStamp
        #return self.Teste01
