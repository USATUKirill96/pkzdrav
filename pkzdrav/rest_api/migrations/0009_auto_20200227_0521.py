# Generated by Django 3.0.3 on 2020-02-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0008_auto_20200226_0345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name': 'Справочник', 'verbose_name_plural': 'Справочники'},
        ),
        migrations.AlterField(
            model_name='directory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='directory',
            unique_together={('directory_id', 'version')},
        ),
    ]
