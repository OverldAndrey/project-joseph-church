# Generated by Django 2.0.5 on 2018-08-09 11:27

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
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 14, 27, 38, 114222)),
        ),
    ]