# Generated by Django 2.1 on 2018-08-08 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_app', '0008_auto_20180809_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 1, 9, 22, 919888)),
        ),
    ]
