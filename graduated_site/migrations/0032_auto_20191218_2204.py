# Generated by Django 3.0 on 2019-12-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0031_auto_20191218_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_internship_post',
            name='content',
            field=models.CharField(help_text='İlan içeriğini giriniz.', max_length=1000, null=True, verbose_name='İçerik'),
        ),
    ]
