# Generated by Django 3.0.3 on 2020-02-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0009_auto_20200227_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='parent_id',
            field=models.IntegerField(default=1, verbose_name='<django.db.models.query_utils.DeferredAttribute object at 0x7fdd9f975340>'),
        ),
    ]