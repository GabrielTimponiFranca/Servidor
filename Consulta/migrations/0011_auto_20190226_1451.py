# Generated by Django 2.1.7 on 2019-02-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consulta', '0010_auto_20190226_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='hist_trafoa',
            name='CorrenteA',
            field=models.FloatField(blank=True, db_column='CorrenteA', null=True),
        ),
        migrations.AddField(
            model_name='hist_trafoa',
            name='CorrenteB',
            field=models.FloatField(blank=True, db_column='CorrenteB', null=True),
        ),
        migrations.AddField(
            model_name='hist_trafoa',
            name='CorrenteC',
            field=models.FloatField(blank=True, db_column='CorrenteC', null=True),
        ),
    ]
