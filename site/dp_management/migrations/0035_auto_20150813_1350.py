# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0034_auto_20150813_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodelproperty',
            name='name',
            field=models.CharField(max_length=56),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 13, 50, 29, 483752), null=True),
            preserve_default=True,
        ),
    ]
