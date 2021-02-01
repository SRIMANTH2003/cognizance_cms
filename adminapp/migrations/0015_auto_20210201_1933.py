# Generated by Django 3.1.4 on 2021-02-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_auto_20210123_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(null=True, upload_to='Achievements'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='organiser',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Profile Pictures'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='evaluator',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('Naresh Kumar', 'Naresh Kumar'), ('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
    ]
