# Generated by Django 3.0 on 2019-12-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0007_auto_20191218_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_internship_post',
            name='working_area',
            field=models.ManyToManyField(related_name='alan', to='graduated_site.working_area', verbose_name='Çalışma Alanları'),
        ),
    ]
