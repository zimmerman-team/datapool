# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0038_auto_20150813_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='remove_prop_strings',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstream',
            name='chart_type',
            field=models.IntegerField(default=0, choices=[(0, b'heat_map'), (1, b'country_map'), (2, b'bar_chart'), (3, b'line_chart')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 13, 5, 24, 250280), null=True),
            preserve_default=True,
        ),
    ]
