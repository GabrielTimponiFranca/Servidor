# Generated by Django 2.1.7 on 2019-02-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consulta', '0008_auto_20190226_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hist_trafoa',
            old_name='Data',
            new_name='E3TimeStamp',
        ),
    ]
