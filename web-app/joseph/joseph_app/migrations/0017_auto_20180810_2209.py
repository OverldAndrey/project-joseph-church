# Generated by Django 2.0.5 on 2018-08-10 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_app', '0016_auto_20180810_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.CharField(default=' ', max_length=127),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 22, 9, 4, 633893)),
        ),
    ]
