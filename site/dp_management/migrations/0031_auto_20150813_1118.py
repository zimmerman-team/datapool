# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0030_auto_20150812_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelproperty',
            name='unpacking_script',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datamodelproperty',
            name='property_type',
            field=models.IntegerField(default=0, choices=[(0, b'STRING'), (1, b'INTEGER'), (2, b'FLOAT'), (3, b'TEXT'), (4, b'DATE'), (5, b'DATETIME'), (6, b'LAT'), (7, b'LONG'), (8, b'LAT LONG'), (9, b'SCRIPT')]),
            preserve_default=True,
        ),
    ]
