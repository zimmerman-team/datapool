# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dp_management', '0025_datamodelproperty_orient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodelproperty',
            name='defaul_value',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datamodelproperty',
            name='property_values',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
