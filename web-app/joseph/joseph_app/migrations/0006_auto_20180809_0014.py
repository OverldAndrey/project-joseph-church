# Generated by Django 2.0.5 on 2018-08-08 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_app', '0005_auto_20180809_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='poll_image',
            field=models.CharField(default=' ', max_length=127),
        ),
        migrations.AddField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 0, 14, 38, 137363)),
        ),
    ]
