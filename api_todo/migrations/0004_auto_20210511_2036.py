# Generated by Django 3.2 on 2021-05-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_todo', '0003_auto_20210511_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]