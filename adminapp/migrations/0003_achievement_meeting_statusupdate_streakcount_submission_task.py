# Generated by Django 3.1.4 on 2021-01-11 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_auto_20210111_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('achievers', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='Achievements/')),
                ('date', models.DateField(null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500, null=True)),
                ('venue', models.DateTimeField(max_length=200, null=True)),
                ('organiser', models.CharField(choices=[], max_length=200, null=True)),
                ('group', models.CharField(choices=[], max_length=200, null=True)),
                ('meeting_link', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Expired', 'Expired'), ('Cancelled', 'Cancelled')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(null=True)),
                ('fullname', models.CharField(max_length=200, null=True)),
                ('score', models.FloatField(max_length=50, null=True)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('submission_file', models.FileField(null=True, upload_to='')),
                ('submission_text', models.CharField(max_length=500, null=True)),
                ('evaluator', models.CharField(choices=[], max_length=200, null=True)),
                ('feedback', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('goal', models.CharField(max_length=500, null=True)),
                ('author', models.CharField(choices=[], max_length=200, null=True)),
                ('content', models.TextField(max_length=2000, null=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('starting_time', models.DateTimeField(null=True)),
                ('max_score', models.FloatField(null=True)),
                ('group', models.CharField(choices=[], max_length=200, null=True)),
                ('resource_file', models.FileField(null=True, upload_to='')),
                ('submission_link', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Streakcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streak', models.IntegerField(null=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminapp.member')),
            ],
        ),
    ]
