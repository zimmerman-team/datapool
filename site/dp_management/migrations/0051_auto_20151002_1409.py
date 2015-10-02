# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0050_auto_20150915_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetstream',
            name='chart_type',
            field=models.IntegerField(default=0, choices=[(0, b'heat_map'), (2, b'bar_chart')]),
            preserve_default=True,
        ),
    ]
