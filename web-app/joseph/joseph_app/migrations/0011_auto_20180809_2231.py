# Generated by Django 2.0.5 on 2018-08-09 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_app', '0010_auto_20180809_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_poll_choice',
            name='choice_mult',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 22, 31, 57, 890282)),
        ),
    ]
