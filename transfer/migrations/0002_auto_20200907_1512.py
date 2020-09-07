# Generated by Django 3.0rc1 on 2020-09-07 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_fname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_lname',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='feed',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='user_feedback',
        ),
    ]
