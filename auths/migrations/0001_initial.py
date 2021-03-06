# Generated by Django 3.0 on 2019-12-20 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='foreign_language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50, verbose_name='Yabancı Diller')),
            ],
            options={
                'verbose_name_plural': 'Yabancı Diller',
            },
        ),
        migrations.CreateModel(
            name='working_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50, verbose_name='Çalışma Alanı')),
            ],
            options={
                'verbose_name_plural': 'Çalışma Alanı',
            },
        ),
        migrations.CreateModel(
            name='working_position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, verbose_name='Çalışma Pozisyonu')),
            ],
            options={
                'verbose_name_plural': 'Çalışma Pozisyonu',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=1000, null=True, verbose_name='Hakkımda')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profil Fotoğrafı')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi')),
                ('certificate', models.CharField(blank=True, max_length=500, null=True, verbose_name='Sertifikalar')),
                ('education', models.CharField(blank=True, max_length=500, null=True, verbose_name='Eğitim Bilgileriniz')),
                ('foreign_language', models.ManyToManyField(blank=True, help_text='Hakimi Olduğunuz Yabancı Dilleri Seçiniz(Varsa)', related_name='yabancı_dil', to='auths.foreign_language', verbose_name='Yabancı Diller')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
                ('working_area', models.ManyToManyField(help_text='Çalışma Alanınızı Seçiniz', related_name='alan', to='auths.working_area', verbose_name='Çalışma Alanı')),
                ('working_position', models.ManyToManyField(help_text='Çalışma Pozisyonunuzu Seçiniz', related_name='pozisyon', to='auths.working_position', verbose_name='Çalışma Pozisyonu')),
            ],
            options={
                'verbose_name_plural': 'Kullanıcı Profilleri',
            },
        ),
    ]
