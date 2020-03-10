# Generated by Django 3.0 on 2019-12-25 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auths', '0007_auto_20191225_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_message_box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, null=True, verbose_name='Mesajınız')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gönderilen_kullanıcı', to=settings.AUTH_USER_MODEL, verbose_name='Mesaj Gönderilecek Kullanıcı')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gönderen_kullanıcı', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
