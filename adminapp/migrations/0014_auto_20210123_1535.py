# Generated by Django 3.1.4 on 2021-01-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_auto_20210123_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusupdate',
            name='reportdate',
        ),
        migrations.RemoveField(
            model_name='statusupdate',
            name='time',
        ),
        migrations.AddField(
            model_name='statusupdate',
            name='reportdatetime',
            field=models.DateTimeField(null=True),
        ),
    ]
