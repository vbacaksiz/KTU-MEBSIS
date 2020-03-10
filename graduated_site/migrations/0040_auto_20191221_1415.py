# Generated by Django 3.0 on 2019-12-21 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graduated_site', '0039_auto_20191221_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_internship_post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
