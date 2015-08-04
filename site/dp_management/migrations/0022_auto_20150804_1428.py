# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0021_auto_20150804_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetstreamproperty',
            name='use_property',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstreamproperty',
            name='action',
            field=models.IntegerField(default=0, choices=[(0, b'FILTER'), (1, b'SEARCHBOX'), (2, b'BETWEEN'), (3, b'MIN'), (4, b'MAX'), (5, b'SUM'), (6, b'AVG'), (7, b'GROUP BY')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstreamproperty',
            name='data_set_stream',
            field=models.ForeignKey(related_name='properties', to='dp_management.DataSetStream'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasetstreamproperty',
            name='data_stream_class',
            field=models.ForeignKey(related_name='my_properties', to='dp_management.DataModelClass'),
            preserve_default=True,
        ),
    ]
