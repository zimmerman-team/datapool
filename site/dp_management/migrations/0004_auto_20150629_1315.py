# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0003_auto_20150629_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='update_interval',
            field=models.CharField(default=b'month', max_length=20, choices=[(b'day', b'Day'), (b'week', b'Week'), (b'month', b'Month'), (b'year', b'Year')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='data_type',
            field=models.IntegerField(default=0, choices=[(0, b'CSV'), (1, b'XML'), (2, b'JSON'), (3, b'FROM QUERY')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
