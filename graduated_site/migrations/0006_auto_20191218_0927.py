# Generated by Django 3.0 on 2019-12-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0005_user_internship_post_working_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_internship_post',
            name='working_area',
            field=models.ManyToManyField(null=True, related_name='alan', to='graduated_site.working_area'),
        ),
        migrations.AlterField(
            model_name='working_area',
            name='area',
            field=models.CharField(max_length=50, verbose_name='Çalışma Alanı'),
        ),
    ]
