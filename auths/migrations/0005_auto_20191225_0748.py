# Generated by Django 3.0 on 2019-12-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0004_user_work_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='foreign_language',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='foreign_language',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Yabancı Diller'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='working_area',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='working_area',
            field=models.CharField(blank=True, choices=[('None', 'Çalışma Alanınızı Seçiniz'), ('yapay zeka', 'YAPAY ZEKA'), ('ses işleme', 'SES İŞLEME'), ('görüntü işleme', 'GÖRÜNTÜ İŞLEME'), ('adli bilişim', 'ADLİ BİLİŞİM')], max_length=25, null=True, verbose_name='Çalışma Alanı'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='working_position',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='working_position',
            field=models.CharField(blank=True, choices=[('None', 'Çalışma Pozisyonunuzu Seçiniz'), ('stajyer', 'STAJYER'), ('menajer', 'MENAJER'), ('programcı', 'PROGRAMCI'), ('tekniker', 'TEKNİKER')], max_length=25, null=True, verbose_name='Çalışma Pozisyonu'),
        ),
        migrations.DeleteModel(
            name='foreign_language',
        ),
        migrations.DeleteModel(
            name='working_area',
        ),
        migrations.DeleteModel(
            name='working_position',
        ),
    ]
