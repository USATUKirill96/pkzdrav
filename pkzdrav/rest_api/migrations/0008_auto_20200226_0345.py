# Generated by Django 3.0.3 on 2020-02-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_auto_20200226_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='version',
            field=models.CharField(max_length=250, verbose_name='Версия'),
        ),
    ]
