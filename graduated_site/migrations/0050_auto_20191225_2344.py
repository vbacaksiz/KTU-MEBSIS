# Generated by Django 3.0 on 2019-12-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0049_auto_20191225_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_model',
            name='graduated_program',
            field=models.CharField(blank=True, choices=[(None, 'Lütfen Mezun Olduğunuz Programı Seçin'), ('LİSANS 1.ÖĞRETİM', 'LİSANS 1.ÖĞRETİM'), ('LİSANS 2.ÖĞRETİM', 'LİSANS 2.ÖĞRETİM'), ('YÜKSEK LİSANS', 'YÜKSEK LİSANS'), ('DOKTORA', 'DOKTORA')], max_length=30, null=True, verbose_name='Mezun Olduğunuz Program'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='graduated_state',
            field=models.CharField(blank=True, choices=[(None, 'Lütfen Mezuniyet Durumunuzu Seçiniz'), ('YENİ MEZUN', 'YENİ MEZUN'), ('GEÇMİŞ YILLARDA MEZUN OLDUM', 'GEÇMİŞ YILLARDA MEZUN OLDUM')], max_length=30, null=True, verbose_name='Mezuniyet Durumunuz'),
        ),
    ]
