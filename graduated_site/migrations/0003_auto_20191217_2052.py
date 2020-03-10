# Generated by Django 3.0 on 2019-12-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0002_auto_20191214_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_internship_post',
            options={'ordering': ['deadline'], 'verbose_name_plural': 'userInthernshipPost'},
        ),
        migrations.AddField(
            model_name='user_internship_post',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='deadline',
            field=models.DateField(null=True, verbose_name='Son Başvuru Tarihi'),
        ),
    ]
