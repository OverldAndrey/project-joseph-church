# Generated by Django 2.0.5 on 2018-08-10 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_app', '0013_auto_20180810_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 15, 12, 31, 919938)),
        ),
    ]