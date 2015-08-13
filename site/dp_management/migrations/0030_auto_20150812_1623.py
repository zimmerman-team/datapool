# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0029_datamodelclass_orient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelproperty',
            name='time_format',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datamodelproperty',
            name='property_type',
            field=models.IntegerField(default=0, choices=[(0, b'STRING'), (1, b'INTEGER'), (2, b'FLOAT'), (3, b'TEXT'), (4, b'DATE'), (5, b'DATETIME')]),
            preserve_default=True,
        ),
    ]
