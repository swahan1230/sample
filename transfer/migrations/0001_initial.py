# Generated by Django 3.0rc1 on 2020-09-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fname', models.CharField(max_length=40)),
                ('user_lname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='user_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('feed', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.user')),
            ],
        ),
    ]
