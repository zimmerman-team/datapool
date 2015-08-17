# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0037_auto_20150813_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetstream',
            name='chart_type',
            field=models.IntegerField(default=0, choices=[(0, b'heat map'), (1, b'country map'), (2, b'bar chart'), (3, b'line chart')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasetstreamproperty',
            name='x_axis',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 16, 28, 57, 107054), null=True),
            preserve_default=True,
        ),
    ]
