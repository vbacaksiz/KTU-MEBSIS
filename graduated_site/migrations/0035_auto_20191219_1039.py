# Generated by Django 3.0 on 2019-12-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduated_site', '0034_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='graduated_site.user_internship_post'),
        ),
    ]
