# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0032_auto_20150813_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodelproperty',
            name='data_model_subgroup',
            field=models.ForeignKey(blank=True, to='dp_management.DataModelSubGroup', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datamodelproperty',
            name='script',
            field=models.ForeignKey(blank=True, to='dp_management.DataModelScript', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datasource',
            name='date_last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 12, 25, 39, 491569), null=True),
            preserve_default=True,
        ),
    ]
