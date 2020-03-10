# Generated by Django 3.0 on 2019-12-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0045_auto_20191222_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_internship_post',
            name='period_internship',
            field=models.CharField(blank=True, choices=[(None, 'Lütfen Staj Dönemini Seçiniz'), ('YAZ', 'YAZ'), ('BAHAR', 'BAHAR'), ('KIŞ', 'KIŞ'), ('GÜZ', 'GÜZ')], max_length=25, null=True, verbose_name='Staj Dönemi'),
        ),
        migrations.AddField(
            model_name='user_internship_post',
            name='time_internship',
            field=models.CharField(blank=True, choices=[(None, 'Lütfen Staj Süresini Seçiniz'), ('30 GÜN', '30 GÜN'), ('60 GÜN', '60 GÜN')], max_length=25, null=True, verbose_name='Staj Süresi'),
        ),
    ]
