# Generated by Django 3.1.4 on 2021-01-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Administrator', 'Administrator')], max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('github_username', models.CharField(max_length=50, null=True)),
                ('discord_handle', models.CharField(max_length=50, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
                ('streak', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('github_username', models.CharField(max_length=50, null=True)),
                ('discord_handle', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
