# Generated by Django 3.0 on 2020-03-07 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import graduated_site.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graduated_site', '0050_auto_20191225_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='survey_model',
            options={'verbose_name_plural': 'Surveys'},
        ),
        migrations.AlterModelOptions(
            name='user_internship_post',
            options={'ordering': ['deadline'], 'verbose_name_plural': 'Announcements'},
        ),
        migrations.AlterModelOptions(
            name='working_area',
            options={'verbose_name_plural': 'Workspace'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='company',
            name='adress',
            field=models.CharField(max_length=200, null=True, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=25, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_sector',
            field=models.ManyToManyField(help_text='Select the workspaces.(Multiple selectable.)', related_name='sector', to='graduated_site.working_area', verbose_name='Company Industry'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(max_length=25, null=True, verbose_name='Company Type'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='E-mail *'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='graduated_program',
            field=models.CharField(blank=True, choices=[(None, 'Please select the program you graduated from'), ('Undergraduate 1.Education', 'Undergraduate 1.Education'), ('Undergraduate 2.Education', 'Undergraduate 2.Education'), ('Graduate', 'Graduate'), ('Doctorate', 'Doctorate')], max_length=30, null=True, verbose_name='The Program You Graduated From'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='graduated_state',
            field=models.CharField(blank=True, choices=[(None, 'Please select your graduation status'), ('New Graduated', 'New Graduated'), ('Graduated in the past year', 'Graduated in the past year')], max_length=30, null=True, verbose_name='Graduation Status'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='graduated_year',
            field=models.CharField(max_length=4, null=True, verbose_name='Graduation Year *'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='name_surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Name Surname *'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, verbose_name='Phone Number *'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='social_profile',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Your Social Media Profile Page'),
        ),
        migrations.AlterField(
            model_name='survey_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='adv_type',
            field=models.CharField(choices=[(None, 'Please select ad type'), ('0', 'STAJ'), ('1', 'İŞ')], max_length=10, null=True, verbose_name='Select Ad Type'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='graduated_site.company', verbose_name='Select Company'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='content',
            field=models.CharField(help_text='Enter the content of the post.', max_length=1000, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='deadline',
            field=models.DateField(null=True, verbose_name='Deadline'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='image',
            field=models.ImageField(blank=True, help_text='You can add photo.', null=True, upload_to=graduated_site.models.upload_to, verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='period_internship',
            field=models.CharField(blank=True, choices=[(None, 'Please select internship period'), ('YAZ', 'YAZ'), ('BAHAR', 'BAHAR'), ('KIŞ', 'KIŞ'), ('GÜZ', 'GÜZ')], max_length=25, null=True, verbose_name='İnternship Period'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='time_internship',
            field=models.CharField(blank=True, choices=[(None, 'Please select internship duration'), ('30 GÜN', '30 GÜN'), ('60 GÜN', '60 GÜN')], max_length=25, null=True, verbose_name='İnternship Duration'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='title',
            field=models.CharField(help_text='Enter the title of the post.', max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user_internship_post',
            name='working_area',
            field=models.ManyToManyField(blank=True, help_text='Choose the workspace you want.(Multiple selectable.)', related_name='Workspace', to='graduated_site.working_area', verbose_name='Workspace'),
        ),
        migrations.AlterField(
            model_name='working_area',
            name='area',
            field=models.CharField(max_length=50, verbose_name='Workspace'),
        ),
    ]
