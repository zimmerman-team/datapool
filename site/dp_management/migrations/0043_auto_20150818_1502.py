# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0042_auto_20150818_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasetstreamproperty',
            name='x_axis',
        ),
        migrations.AddField(
            model_name='datasetstream',
            name='x_axis',
            field=models.ForeignKey(blank=True, to='dp_management.DataSetStreamProperty', null=True),
            preserve_default=True,
        ),
    ]
