# Generated by Django 3.0 on 2019-12-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Eğitim Bilgileri'),
        ),
    ]
